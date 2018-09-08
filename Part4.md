# ЧАСТЬ IV Введение в информатику

<!-- TOC -->

- [ЧАСТЬ IV Введение в информатику](#часть-iv-введение-в-информатику)
    - [Глава 21. Структуры данных](#глава-21-структуры-данных)
        - [Структуры данных](#структуры-данных)
        - [Стеки](#стеки)
        - [Изменение порядка символов строки при помощи стека](#изменение-порядка-символов-строки-при-помощи-стека)
        - [Очереди](#очереди)
        - [Словарь терминов Глава 21](#словарь-терминов-глава-21)
    - [Глава 22. Алгоритмы](#глава-22-алгоритмы)
        - [Последовательный поиск](#последовательный-поиск)
        - [Палиндром](#палиндром)
        - [Анаграмма](#анаграмма)
        - [Рекурсия](#рекурсия)
        - [Словарь терминов Глава 22](#словарь-терминов-глава-22)

<!-- /TOC -->

## Глава 21. Структуры данных

> Вообще-то я утверждаю, что разница между плохим программистом
> и хорошим закл ючается в том, что именно он считает более важным — свой
> код или свои структуры данных. Плохие программисты беспокоятся о коде.
> Хорошие программисты беспокоятся о структурах данных и их отношениях.
> *Линус Торвальдс*

### Структуры данных

**Структура данных** — это формат, используемый для хранения и организации информации. Структуры данных — фундаментальное понятие в программировании, они встроены в большинство языков. Вы уже знаете, как пользоваться некоторыми встроенными в Python структурами данных — списками, кортежами и словарями. В этой главе вы научитесь создавать еще две структуры данных — стеки и очереди.

### Стеки

Стек — это структура данных. Как и в список, в стек можно добавлять элементы и удалять их из него, но в отличие от списка, вы можете добавлять и удалять только последний элемент. Если у вас есть список [1, 2, 3], вы можете удалить из него любой элемент. Если у вас есть такой же стек, вы можете удалить лишь последний элемент, 3, и тогда стек будет иметь вид [1, 2]. Теперь можно удалить 2, а после этого — 1, и стек станет пустым. Удаление элемента из стека обозначается термином **pop**. Если вы поместите 1 обратно в стек, он будет иметь вид [1], а если затем поместите двойку, то [1, 2]. Добавление элемента в стек обозначается словом **push**. Такой вид структуры данных, при котором последний помещенный элемент является первым извлекаемым, называется структурой данных «**последним вошел — первым вышел**» (**LIFO**, last-in-first-out).  
LIFO можно представить как стопку тарелок. Если вы сложите пять тарелок одну на другую и захотите вытащить ту, что в самом низу, вам сначала придется убрать все верхние. Каждый фрагмент данных в стеке сродни тарелке, чтобы получить к нему доступ, нужно избавиться от данных сверху.  
У стека будет пять методов: `is_empty, push, pop, peek и size.` Метод `is_empty` возвращает значение `True` если ваш стек пуст, и `False` в противном случае. Метод `push` добавляет элемент на «вершину» стека, `pop` удаляет и возвращает элемент с «вершины» стека, `peek` возвращает этот элемент, но не удаляет его. Метод `size` возвращает целое число, представляющее количество элементов в стеке.

### Изменение порядка символов строки при помощи стека

Стек может изменять направление итерируемого элемента на обратное, поскольку все, что вы поместите в стек, отделяется в обратном порядке.

```python
reverse = ""
for _ in range(stack.size()):
    reverse += stack.pop()
```

### Очереди

Очередь — еще одна структура данных. Она тоже похожа на список; вы можете добавлять в нее элементы и удалять их. Очередь также напоминает стек, поскольку добавлять и удалять элементы можно лишь в определенном порядке. В отличие от стека, где первый помещенный элемент является последним извлекаемым, очередь представляет собой структуру данных вида «**первым вошел — первым вышел**» (**FIFO**, first-in-first-out): первый помещенный элемент является первым извлекаемым.  
Представьте FIFO как очередь людей, желающих купить билеты в кино. Первый человек в очереди — это первый человек, который купит билеты, второй человек в очереди — второй, кто купит билеты, и так далее.  
В этом разделе вы построите очередь, используя четыре метода: `enqueue, dequeue, is_empty` и `size`. `enqueue` добавляет новый элемент в очередь; `dequeue` удаляет элемент из очереди; `is_empty` проверяет, пуста ли очередь, и возвращает соответственно `True` либо `False`; `size` возвращает количество элементов в очереди.  

### Словарь терминов Глава 21

**FIFO:** сокращение от англ. `first-in-first-out` — «первым вошел — первым вышел».  
**LIFO:** сокращение от англ. `last-in-first-out` — «последним вошел — первым вышел».  
**Pop:** удаление элемента из стека.  
**Push:** добавление элемента в стек.  
**Очередь:** структура данных вида «первым вошел — первым вышел».  
**Стек:** структура данных вида «последним вошел — первым вышел».  
**Структура данных «первым вошел — первым вышел»:** структура данных, в которой первый помещенный элемент является первым извлекаемым.  
**Структура данных «последним вошел — первым вышел»:** вид структуры данных, при котором последний помещенный элемент является первым извлекаемым.  
**Структура данных:** формат, используемый для хранения и организации информации.  
**Эпоха:** момент во времени, используемый в роли ссылки.

## Глава 22. Алгоритмы

> Алгоритм подобен кулинарному рецепту.
> *Васим Латиф*

### Последовательный поиск

**Поисковый алгоритм** находит информацию в структуре данных, например в списке. **Последовательный поиск** — это простой поисковый алгоритм, который проверяет каждый элемент в структуре данных на предмет его соответствия тому, что алгоритм ищет.

### Палиндром

**Палиндром** — это слово, которое одинаково записывается в обоих направлениях. Вы можете написать алгоритм, который будет проверять, является ли слово палиндромом, меняя порядок букв в нем на обратный и сравнивая измененное слово с исходным. Если измененное и исходное слово записываются одинаково, значит, исходное слово было палиндромом.

### Анаграмма

**Анаграмма** — это слово, созданное путем перестановки букв другого слова. Слово «тапок» является анаграммой слова «капот», поскольку каждое из этих слов может быть получено путем перестановки букв другого слова. Определить, являются ли два слова анаграммами, можно отсортировав буквы каждого из них в алфавитном порядке и проверив, одинаковые ли они.

### Рекурсия

**Рекурсия** — это способ решения проблем, который предполагает разбивание проблемы на все меньшие и меньшие фрагменты, пока проблема не решается элементарно. До сих пор вы решали проблемы, используя **итерационные алгоритмы.** Итерационные алгоритмы решают проблемы путем повторения шагов снова и снова, обычно при помощи цикла. **Рекурсивные (рекуррентные) алгоритмы** полагаются только на функции, которые вызывают сами себя. Любую проблему, которую можно решить итерационно, можно решить рекурсивно, но иногда рекурсивный алгоритм представляет собой более изящное решение.  
Рекурсивный алгоритм создается внутри функции. Функция должна содержать **базовый случай** — условие, завершающее рекурсивный алгоритм, не позволяющее ему продолжаться вечно. Внутри функции функция вызывает себя сама. Каждый раз, как функция вызывает себя сама, она продвигается ближе к базовому случаю. В конце концов, выполняется условие базового случая, проблема решается, и функция перестает вызывать себя. Алгоритм, следующий таким правилам, отвечает трем законам рекурсии.  

1. Рекурсивный алгоритм должен содержать базовый случай.
2. Рекурсивный алгоритм должен изменять свое состояние и двигаться по направлению к базовому случаю.
3. Рекурсивный алгоритм должен вызывать сам себя.

### Словарь терминов Глава 22

**Алгоритм:** серия шагов, которым следуют для решения проблемы.  
**Анаграмма:** слово, созданное путем перестановки букв другого слова.  
**Базовый случай:** условие, завершающее рекурсивный алгоритм.  
**Итерационный алгоритм:** решает проблемы путем повторения шагов снова и снова, обычно используя цикл.  
**Палиндром:** слово, которое одинаково записывается в обоих направлениях.  
**Поисковый алгоритм:** алгоритм, который находит информацию в структуре данных, например в списке.  
**Последовательный поиск:** простой поисковый алгоритм для поиска информации в структуре данных, который проверяет каждый элемент в ней на предмет его соответствия тому, что алгоритм ищет.  
**Рекурсивный (рекуррентный) алгоритм:** рекурсивные алгоритмы используют функции, которые вызывают сами себя.  
**Рекурсия:** способ решения проблем, который предполагает разбивание проблемы на все меньшие и меньшие фрагменты, пока проблема не решается элементарно.