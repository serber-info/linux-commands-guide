import copy
import json
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from guia_linux.catalog import catalog_from_data, load_catalog

ROOT = Path(__file__).resolve().parents[1] / 'guia_linux/content/tools'


@pytest.fixture
def document():
    return json.loads((ROOT / 'wc.json').read_text())


@pytest.mark.parametrize('mutation', ['missing-en', 'duplicate-id', 'unknown-field', 'control', 'bad-effect', 'bad-ref', 'empty-sources', 'bad-quick'])
def test_invalid_content_is_rejected(document, mutation):
    d = copy.deepcopy(document)
    if mutation == 'missing-en':
        del d['title']['en']
    elif mutation == 'duplicate-id':
        d['examples'].append(copy.deepcopy(d['examples'][0]))
    elif mutation == 'unknown-field':
        d['surprise'] = True
    elif mutation == 'control':
        d['examples'][0]['text'] += '\x1b[2J'
    elif mutation == 'bad-effect':
        d['examples'][0]['effect'] = 'safe-always'
    elif mutation == 'bad-ref':
        d['examples'][0] = {'ref': 'missing.id'}
    elif mutation == 'empty-sources':
        d['sources'] = []
    else:
        d['examples'][0]['quick'] = 'yes'
    with pytest.raises(ValueError):
        catalog_from_data([d])


def test_unknown_related_and_duplicate_alias(document):
    document['related'] = ['missing']
    with pytest.raises(ValueError):
        catalog_from_data([document])
    document['related'] = []
    document['aliases'] = ['wc']
    with pytest.raises(ValueError):
        catalog_from_data([document])


def test_model_and_mapping_are_immutable():
    catalog = load_catalog()
    with pytest.raises(FrozenInstanceError):
        catalog.get('wc').name = 'changed'
    with pytest.raises(TypeError):
        catalog.tools['bad'] = catalog.get('wc')


def test_basics_share_definitions_with_system():
    catalog = load_catalog()
    system = {e.id: e for e in catalog.get('system').examples}
    for entry in catalog.get('ls').examples:
        assert entry is system[entry.id]


def test_search_alias_accents_and_deduplication():
    catalog = load_catalog()
    assert catalog.get('BATCAT') is catalog.get('bat')
    assert catalog.get('fdfind') is catalog.get('fd')
    assert catalog.search('numero linea') == catalog.search('número línea')
    assert not catalog.search(' ')
    results = catalog.search('file')
    assert len({e.id for _, e in results}) == len(results)
    assert all(t.name == 'grep' for t, _ in catalog.search('file', 'grep'))


def test_dangerous_examples_keep_warnings():
    catalog = load_catalog()
    for name, fragment in [('git', 'reset --hard'), ('find', '-delete'), ('iptables', '-F'), ('ssh', 'StrictHostKeyChecking=no'), ('curl', 'curl -k')]:
        entry = next(e for e in catalog.get(name).examples if fragment in e.text)
        assert entry.effect in {'delete', 'admin', 'sensitive'}
        assert catalog.get(name).notes.es and catalog.get(name).notes.en


def test_no_colors_in_content():
    for path in ROOT.glob('*.json'):
        assert '\x1b' not in path.read_text()
        assert r'\u001b' not in path.read_text()


def test_all_original_fiches_and_rows_survive_migration():
    baseline = json.loads((Path(__file__).parent / 'fixtures/legacy_ids.json').read_text())
    catalog = load_catalog()
    assert len(baseline) == 51
    for name, ids in baseline.items():
        current = [e.id for e in catalog.get(name).examples if e.id in set(ids)]
        assert current == ids, name


@pytest.mark.parametrize('reserved', ['learn', 'practice', 'list'])
def test_reserved_names_are_not_hidden_by_cli(document, reserved):
    document['name'] = reserved
    with pytest.raises(ValueError):
        catalog_from_data([document])


def test_curated_tasks_are_discoverable_without_knowing_the_tool():
    catalog = load_catalog()
    assert 'find' in {t.name for t, _ in catalog.search('buscar archivos')}
    assert 'cp' in {t.name for t, _ in catalog.search('copiar archivos')}
    assert 'wc' in {t.name for t, _ in catalog.search('contar líneas')}
