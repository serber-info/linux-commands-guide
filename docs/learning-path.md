# Learning path / Ruta de aprendizaje

## First session

1. `lh learn navigation`: locate yourself and understand paths.
2. `lh ls --quick`, `lh cd --explain`: inspect before changing directories.
3. `lh learn quoting`: one path is not always one argument without quotes.
4. `lh learn help`: learn how to leave a pager/editor and find installed manuals.

## Combine tools

1. `lh learn globs`: filenames versus text patterns.
2. `lh grep --explain`, `lh practice grep`: inspect sample log lines.
3. `lh learn pipes`, `lh practice pipes`: sort and count.
4. `lh learn redirections`, `lh learn exit-status`: files and success conditions.
5. `lh practice wc`, `lh practice regex`: confirm results with small fixtures.

## Understand your environment

`lh learn environment`, `lh learn permissions`, `lh learn processes`.
Then explore `lh list --category system` and `lh list --category network`.
Use query examples first, not privileged mutations. Advanced entries remain available, but learning
Docker, LXC or firewall changes is not a prerequisite for everyday terminal work.

## Practice contract

Practices display setup, task, expected result, optional hints and a solution. They do not execute
commands, create directories, inspect user files or store progress. You manually copy preparation into
your shell; it uses a new temporary directory. Continue only after successful setup. Files remain
there for inspection; lh does not delete them automatically. No root or external hosts are needed.
