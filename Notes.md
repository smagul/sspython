# ЧАСТЬ I Введение в программирование

## Глава 2. Начало работы

### Словарь терминов

**Python:** простой в чтении язык программирования с открытым исходным кодом, который вы научитесь использовать в этой книге. Создан Гвидо ван Россумом и назван в честь британской комедийной труппы «Монти Пайтон».  
**Высокоуровневый язык программирования:** язык программирования, который больше похож на английский, чем язык программирования низкого уровня.  
**Код:** инструкции компьютеру, которые пишут программисты.  
**Низкоуровневый язык программирования:** язык программирования, запись которого ближе к двоичному формату (0 и 1), чем записи языка программирования высокого уровня.  
**Программирование:** написание инструкций, которые выполняет компьютер.  
**Язык ассемблера:** тип трудного для чтения языка программирования.  

## Глава 3. Введение в программирование

### Комментарии

**Комментарий** — это строка (или часть строки) кода, написанная на русском (или любом другом языке), которой предшествует специальный символ, указывающий языку программирования игнорировать эту строку (или часть строки) кода. В Python для создания комментариев используется символ `#`. Пишите комментарий только в том случае, если в своем коде вы делаете чтото необычное или объясняете то, что не является очевидным исходя из самого кода. Используйте комментарии экономно — не комментируйте каждую строку кода — храните их для особых ситуаций.

### Строки кода

Иногда фрагмент кода слишком длинный и не вмещается в одну строку. Код, помещенный в тройные кавычки, круглые, квадратные и фигурные скобки, может быть продолжен на следующей строке.

```python
print("""Это очень очень очень
        очень очень очень длинная
        строка кода.""")
```

Также, чтобы продолжить код на следующей строке, можно использовать символ обратного слеша (`\`).

```python
print\
("""Это очень очень очень очень очень
очень длинная строка кода.""")
```

### Типы данных

Данные в Python сгруппированы в различные категории, называемые **типами данных**. В Python каждое значение, например `2` или `"Hello, world!"`, называется **объектом**.  

`"Hello, world!"` — объект с типом данных **str**. **Символ** — это один знак, вроде `a` или `1`.  
Целые числа (1, 2, 3, 4 и т.д.) имеют тип данных **int**.  
Вещественные числа (числа с десятичной точкой) имеют тип данных **float**.  
Объекты, имеющие тип данных **bool**, называются булевыми или логическими, они принимают значение `True` или `False`.  
Объекты с типом данных **NoneType** всегда имеют значение **None**. Они используются для представления отсутствия значения.  

Часто при программировании необходимо **увеличить** (инкрементировать) или **уменьшить** (декрементировать) значение переменной.

```python
x = 10
x += 1 # 11
x -= 1 # 10
```

### Константы и переменные

**Константа** — это значение, которое никогда не меняется. Каждое число является константой: число два всегда будет представлять значение `2`. **Переменная** же напротив относится к значению, которое может измениться.

Вы можете присваивать переменным любые имена, но должны следовать четырем правилам:

1. Имена переменных не могут содержать пробелы. Если вы хотите использовать в имени два слова, укажите между ними **знак нижнего подчеркивания**: например, `my_variable = "String!"`.
2. Имена переменных могут содержать только **латинские буквы, цифры и символ подчеркивания**.
3. **Нельзя начинать имя переменной с цифры**. И хотя вы можете начинать переменную с подчеркивания, пока что так не делайте — это отдельная тема, которую мы рассмотрим позже.
4. Вы не можете использовать **ключевые слова Python** в качестве имен переменных. Список ключевых слов можно найти по адресу <http://zetcode.com/lang/python/keywords/>.

### Синтаксис

**Синтаксис** — это набор правил, принципов и процессов, которые определяют структуру предложений на определенном языке, в частности, порядок слов. В Python строки всегда берутся в кавычки — это пример синтаксиса Python.

### Ошибки и исключения

У Python есть два типа ошибок: **синтаксические ошибки** и **исключения**. **Исключением** называется любая ошибка, которая не является синтаксической. `ZeroDivisionError` — пример исключения, которое возникает, если вы попытаетесь делить на ноль. Если в своем коде вы неправильно использовали отступы, то получите ошибку `IndentationError`.

### Арифметические операторы