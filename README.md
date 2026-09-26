## Code Coverage

**1. Run tests**

From the `autotests-ui` root:

    coverage run -m pytest -m "regression"

Creates `.coverage`.

**2. Generate HTML report**

    coverage html

Open `htmlcov/index.html` in a browser.

## ui-coverage-tool

**1. Run tests**

From the `autotests-ui` root:

    pytest -m "regression"

Creates `./coverage-results` folder.

**2. Generate HTML report**

    ui-coverage-tool save-report

Creates `index.html`, `coverage-report.json` (same as index.html but for CI/CD), `coverage-history.json`

Open `index.html` in a browser.

