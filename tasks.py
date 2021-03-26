"""
Tasks for maintaining the project.

Execute 'invoke --list' for guidance on using Invoke
"""
import platform
from pathlib import Path

from invoke import task
from invoke.context import Context
from invoke.runners import Result

ROOT_DIR = Path(__file__).parent
TASKS_DIR = ROOT_DIR / 'tasks'
HANDLERS_DIR = ROOT_DIR / 'handlers'
VARS_DIR = ROOT_DIR / 'vars'
DEFAULTS_DIR = ROOT_DIR / 'defaults'
MOLECULE_DIR = ROOT_DIR / 'molecule/default'
META_DIR = ROOT_DIR / 'meta'
ANSIBLE_TARGETS = [
    ROOT_DIR,
    TASKS_DIR,
    HANDLERS_DIR,
    VARS_DIR,
    DEFAULTS_DIR,
    MOLECULE_DIR
]
ANSIBLE_TARGETS_STR = " ".join([str(t) for t in ANSIBLE_TARGETS])


def _run(c: Context, command: str) -> Result:
    return c.run(command, pty=platform.system() != "Windows")


@task()
def install_hooks(c):
    # type: (Context) -> None
    """Install pre-commit hooks."""
    _run(c, "pipenv run pre-commit install")


@task()
def hooks(c):
    # type: (Context) -> None
    """Run pre-commit hooks."""
    _run(c, "pipenv run pre-commit run --all-files")


@task()
def yamllint(c):
    # type: (Context) -> None
    """Run yamllint, a linter for YAML files."""
    _run(c, f"yamllint -c {ROOT_DIR / '.yamllint'} {ROOT_DIR}")


@task()
def ansible_lint(c):
    # type: (Context) -> None
    """Run ansible linter."""
    lint_options = [
        '--force-color',
        '-p',
        '-v',
        '--project-dir' ,
        str(ROOT_DIR)
    ]
    _run(c, f"ansible-lint {' '.join(lint_options)} {ANSIBLE_TARGETS_STR}")


@task(pre=[yamllint, ansible_lint])
def lint(c):
    # type: (Context) -> None
    """Run all linting."""


@task()
def tests(c):
    # type: (Context) -> None
    """Run ansible molecule test."""
    _run(c, f"molecule test")


@task(
    help={
        "part": "Part of the version to be bumped.",
        "dry_run": "Don't write any files, just pretend. (default: False)",
    }
)
def version(c, part, dry_run=False):
    # type: (Context, str, bool) -> None
    """Bump version."""
    bump_options = ["--dry-run"] if dry_run else []
    _run(c, f"pipenv run bump2version {' '.join(bump_options)} {part}")
