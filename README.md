<h1>
  Get Start
</h1>

<h2>
  Step 1: Clone this repo in your root folder or install ZIP file
</h2>

```
git clone https://github.com/ShaidullinArtem/TRPOTesting.git
```

<h2>
    2 Step: Create venv and installing libs
</h2>
<h3>
  In order to craete venv in root directory
</h3>

```
python -m venv venv
```

<h3>
  Activate venv
</h3>

```
.\venv\Scripts\activate
```

<h3>
  Now you can install all necessary libs. Use this command 
</h3>

```
pip install -r requirements.txt
```

<h2>
  Step 3: Uncomment needs web-site classes test in main.py
</h2>

<h3>Example</h3>

```
def main() -> None:

    # TODO  Algoritmika tests
    algoritmika = AlgoritmikaTests('http://algoritmika.org/ru')
    print(algoritmika.header_test('header__logo'))
    # print(algoritmika.is_visible_test('start-section__btn'))
    # algoritmika.nav_to_link_test('https://motka.design/')
    # algoritmika.enter_input_test('sub-email', 'test@gmail.com')
    # algoritmika.click_test('partner-footer__mailing-btn')
```


