## Code Coverage

**1. Install**

    pip install coverage

**2. Run tests**

From the `autotests-ui` root:

    coverage run -m pytest -m "regression"

Creates `.coverage`.

**3. Generate HTML report**

    coverage html

Open `htmlcov/index.html` in a browser.