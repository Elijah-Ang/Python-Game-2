const fs = require('fs');
const path = require('path');

const lessonsPath = path.resolve(__dirname, '../frontend/public/data/lessons.json');
const pythonCoursePath = path.resolve(__dirname, '../frontend/public/data/course-python-basics.json');
const sqlCoursePath = path.resolve(__dirname, '../frontend/public/data/course-sql-fundamentals.json');

const lessons = JSON.parse(fs.readFileSync(lessonsPath, 'utf8'));
const pythonCourse = JSON.parse(fs.readFileSync(pythonCoursePath, 'utf8'));
const sqlCourse = JSON.parse(fs.readFileSync(sqlCoursePath, 'utf8'));

const getChapterLessonIds = (course, chapterId) => {
  const ids = [];
  (course.chapters || []).forEach((chapter) => {
    if (String(chapter.id) !== String(chapterId)) return;
    if (Array.isArray(chapter.lessons)) {
      chapter.lessons.forEach((lesson) => ids.push(String(lesson.id)));
      return;
    }
    (chapter.concepts || []).forEach((concept) => {
      (concept.lessons || []).forEach((lesson) => ids.push(String(lesson.id)));
    });
  });
  return ids;
};

const normalizeTitle = (title) => String(title || '').toLowerCase();

const pythonTemplate = (title) => {
  const lower = normalizeTitle(title);
  const trimmed = lower.trim();
  let content = `# ${title}\n\n## Big idea\n`;
  let analogy = '';
  let example = '';
  let walkthrough = [];
  let prompt = '';
  let starter = '';
  let solution = '';
  let tags = [];

  const finish = () => {
    content += `${analogy ? `${analogy}\n\n` : ''}`;
    content += `## Example\n\`\`\`python\n${example}\n\`\`\`\n\n`;
    if (walkthrough.length) {
      content += `## Walkthrough\n${walkthrough.map((s, i) => `${i + 1}. ${s}`).join('\n')}\n\n`;
    }
    content += `## Your turn\n${prompt}\n`;
    return { content, starter, solution, tags };
  };

  if (lower.includes('global variable')) {
    content += 'Global variables live outside a function so they can be shared, but they must be handled carefully.\n';
    analogy = 'Analogy: a global variable is a bulletin board in a hallway; anyone can read it, and anyone can scribble over it.';
    example = 'count = 0\n\n\ndef bump():\n    global count\n    count += 1\n\nbump()\nprint(count)';
    walkthrough = ['Define a variable outside the function.', 'Use the global keyword to change it inside.', 'Call the function and print.'];
    prompt = 'Update the global variable `visits` inside the function and print the final value.';
    starter = 'visits = 3\n\ndef log_visit():\n    # Use global visits and add 1\n    ...\n\nlog_visit()\nprint(visits)';
    solution = 'visits = 3\n\ndef log_visit():\n    global visits\n    visits += 1\n\nlog_visit()\nprint(visits)';
    tags = ['variables', 'scope'];
    return finish();
  }

  if (lower.includes('variable')) {
    content += 'Variables are names that point to values so you can store and reuse data.\n';
    analogy = 'Analogy: a variable is a labeled box; the label stays the same even if you replace what is inside.';
    example = 'student = "Ava"\npoints = 12\nprint(student)\nprint(points)';
    walkthrough = ['Create a variable with =', 'Use print() to read the value.'];
    prompt = 'Create a variable named `city` with value "Denver" and print it.';
    starter = '# Create a variable named city with value "Denver"\n\n# Print the variable\n';
    solution = 'city = "Denver"\nprint(city)';
    tags = ['variables'];
    return finish();
  }

  if (lower.includes('data type') || lower.includes('type')) {
    content += 'Python has different data types (int, float, str, bool) and you can inspect them with type().\n';
    analogy = 'Analogy: data types are the shapes of containers; a liquid jar cannot hold a hammer without issues.';
    example = 'age = 42\nprice = 19.99\nname = "Jin"\nactive = True\nprint(type(age), type(price), type(name), type(active))';
    walkthrough = ['Create values of different types.', 'Use type() to check each.'];
    prompt = 'Create an int, a float, and a string, then print their types.';
    starter = '# Create values of each type\n\n# Print their types\n';
    solution = 'count = 7\nratio = 0.25\nlabel = "ready"\nprint(type(count), type(ratio), type(label))';
    tags = ['types'];
    return finish();
  }

  if (lower.includes('bytes') || lower.includes('bytearray') || lower.includes('memoryview')) {
    content += 'Bytes are raw binary data. bytearray is mutable, and memoryview lets you view and slice without copying.\n';
    analogy = 'Analogy: bytes are a string of light switches (0/1), and memoryview is a window looking at the same switches.';
    example = 'data = bytes([65, 66, 67])\nmutable = bytearray(data)\nview = memoryview(mutable)\nview[0] = 90\nprint(data)\nprint(mutable)\nprint(bytes(view))';
    walkthrough = ['Create bytes and bytearray.', 'Use memoryview to modify in place.', 'Show the results.'];
    prompt = 'Create a bytearray from [1, 2, 3], change the first element to 9, and print it.';
    starter = 'mutable = bytearray([1, 2, 3])\n# Change the first element to 9\n\nprint(mutable)';
    solution = 'mutable = bytearray([1, 2, 3])\nmutable[0] = 9\nprint(mutable)';
    tags = ['types'];
    return finish();
  }

  if (lower.includes('string')) {
    content += 'Strings store text. You can slice, format, and transform them with built-in methods.\n';
    analogy = 'Analogy: a string is a bracelet of characters; you can pick beads by index or slice a section.';
    if (lower.includes('slicing')) {
      example = 'word = "pineapple"\nprint(word[0])\nprint(word[4:9])\nprint(word[-3:])';
      walkthrough = ['Index with [0] for the first char.', 'Slice with [start:end] (end not included).'];
      prompt = 'Slice the last 4 characters from "notebook".';
      starter = 'word = "notebook"\n# Print the last 4 characters\n';
      solution = 'word = "notebook"\nprint(word[-4:])';
    } else if (lower.includes('format')) {
      example = 'name = "Lee"\nscore = 92\nprint(f"{name} scored {score}.")';
      walkthrough = ['Use f-strings to embed values in text.'];
      prompt = 'Create a message that says "Ava has 3 tasks." using f-strings.';
      starter = 'name = "Ava"\ncount = 3\n# Print the message using an f-string\n';
      solution = 'name = "Ava"\ncount = 3\nprint(f"{name} has {count} tasks.")';
    } else if (lower.includes('escape')) {
      example = 'quote = "She said, \\"hello\\""\npath = "C:\\\\Users\\\\Ava"\nprint(quote)\nprint(path)';
      walkthrough = ['Use backslash to escape quotes and backslashes.'];
      prompt = 'Store the text He said "yes" in a variable and print it.';
      starter = '# Store the text He said "yes"\n';
      solution = 'text = "He said \\"yes\\""\nprint(text)';
    } else if (lower.includes('method') || lower.includes('modify')) {
      example = 'text = "  Data Science  "\nprint(text.strip())\nprint(text.lower())\nprint(text.replace(" ", "-").strip())';
      walkthrough = ['strip() removes outer spaces.', 'lower() makes text lowercase.', 'replace() swaps characters.'];
      prompt = 'Lowercase and strip the text "  READY  ".';
      starter = 'text = "  READY  "\n# Print a cleaned version\n';
      solution = 'text = "  READY  "\nprint(text.strip().lower())';
    } else if (lower.includes('concatenate')) {
      example = 'first = "Ada"\nlast = "Lovelace"\nprint(first + " " + last)';
      walkthrough = ['Use + to join strings.'];
      prompt = 'Concatenate "data" and "class".';
      starter = 'a = "data"\nb = "class"\n# Print the combined string\n';
      solution = 'a = "data"\nb = "class"\nprint(a + b)';
    } else {
      example = 'greeting = "hello"\nprint(greeting.upper())\nprint(greeting.title())';
      walkthrough = ['Call string methods with dot notation.'];
      prompt = 'Print "python" in uppercase.';
      starter = 'word = "python"\n# Print uppercase\n';
      solution = 'word = "python"\nprint(word.upper())';
    }
    tags = ['strings'];
    return finish();
  }

  if (lower.includes('boolean')) {
    content += 'Booleans represent truth values (True/False) and are produced by comparisons.\n';
    analogy = 'Analogy: a boolean is a yes/no switch.';
    example = 'x = 7\nprint(x > 5)\nprint(x == 7)\nprint(x < 3)';
    walkthrough = ['Use comparison operators to produce booleans.'];
    prompt = 'Check whether 10 is not equal to 5 and print the result.';
    starter = 'value = 10\n# Print whether value is not equal to 5\n';
    solution = 'value = 10\nprint(value != 5)';
    tags = ['booleans'];
    return finish();
  }

  if (lower.includes('operator')) {
    content += 'Operators are symbols that perform actions like addition, comparison, or logic.\n';
    analogy = 'Analogy: operators are verbs in code (add, compare, combine).';
    example = 'a = 10\nb = 3\nprint(a + b)\nprint(a > b)\nprint(a % b)';
    walkthrough = ['Arithmetic operators combine numbers.', 'Comparison operators return booleans.'];
    prompt = 'Use % to compute the remainder of 17 divided by 5.';
    starter = 'a = 17\nb = 5\n# Print the remainder\n';
    solution = 'a = 17\nb = 5\nprint(a % b)';
    tags = ['operators'];
    return finish();
  }

  if (lower.includes('list')) {
    content += 'Lists are ordered collections you can mutate (add, remove, change items).\n';
    analogy = 'Analogy: a list is a shopping list that you can reorder or edit.';
    if (lower.includes('remove list duplicates')) {
      example = 'nums = [1, 2, 2, 3]\nunique = list(dict.fromkeys(nums))\nprint(unique)';
      walkthrough = ['dict.fromkeys preserves order while removing duplicates.'];
      prompt = 'Remove duplicates from ["a", "b", "a", "c"] while keeping order.';
      starter = 'letters = [\"a\", \"b\", \"a\", \"c\"]\n# Remove duplicates while preserving order\n';
      solution = 'letters = ["a", "b", "a", "c"]\nunique = list(dict.fromkeys(letters))\nprint(unique)';
    } else if (lower.includes('access')) {
      example = 'items = ["pen", "book", "phone"]\nprint(items[0])\nprint(items[-1])';
      walkthrough = ['Use index 0 for the first item.', 'Use -1 for the last.'];
      prompt = 'Print the second item in ["red", "green", "blue"].';
      starter = 'colors = [\"red\", \"green\", \"blue\"]\n# Print the second item\n';
      solution = 'colors = ["red", "green", "blue"]\nprint(colors[1])';
    } else if (lower.includes('add') || lower.includes('append')) {
      example = 'items = ["a", "b"]\nitems.append("c")\nprint(items)';
      walkthrough = ['append adds one item to the end.'];
      prompt = 'Append "done" to the list.';
      starter = 'tasks = [\"start\", \"work\"]\n# Append \"done\"\n';
      solution = 'tasks = ["start", "work"]\ntasks.append("done")\nprint(tasks)';
    } else if (lower.includes('remove')) {
      example = 'items = ["a", "b", "c"]\nitems.remove("b")\nprint(items)';
      walkthrough = ['remove deletes the first matching item.'];
      prompt = 'Remove "draft" from the list.';
      starter = 'files = [\"draft\", \"final\", \"archive\"]\n# Remove \"draft\"\n';
      solution = 'files = ["draft", "final", "archive"]\nfiles.remove("draft")\nprint(files)';
    } else if (lower.includes('method')) {
      example = 'items = [1, 3, 2]\nitems.sort()\nitems.reverse()\nprint(items)';
      walkthrough = ['sort orders the list.', 'reverse flips the order.'];
      prompt = 'Sort [5, 2, 9] and print.';
      starter = 'nums = [5, 2, 9]\n# Sort and print\n';
      solution = 'nums = [5, 2, 9]\nnums.sort()\nprint(nums)';
    } else {
      example = 'items = ["pen", "book"]\nitems[0] = "marker"\nprint(items)';
      walkthrough = ['Lists are mutable, so you can replace items by index.'];
      prompt = 'Replace the first item in ["old", "new"] with "fresh".';
      starter = 'items = [\"old\", \"new\"]\n# Replace the first item\n';
      solution = 'items = ["old", "new"]\nitems[0] = "fresh"\nprint(items)';
    }
    tags = ['lists'];
    return finish();
  }

  if (lower.includes('tuple')) {
    content += 'Tuples are ordered collections that are immutable (cannot be changed after creation).\n';
    analogy = 'Analogy: a tuple is a sealed package; you can read it, but not modify it.';
    example = 'coords = (10, 20)\nprint(coords[0])';
    walkthrough = ['Use indexes to read tuple values.'];
    prompt = 'Create a tuple (5, 6) and print the second value.';
    starter = 'coords = (5, 6)\n# Print the second value\n';
    solution = 'coords = (5, 6)\nprint(coords[1])';
    tags = ['tuples'];
    return finish();
  }

  if (lower.includes('set')) {
    content += 'Sets store unique items with no guaranteed order.\n';
    analogy = 'Analogy: a set is a bucket of unique stickers; duplicates get ignored.';
    example = 'items = {"a", "b", "a"}\nprint(items)';
    walkthrough = ['Duplicate values collapse into one.'];
    prompt = 'Add "kiwi" to a set and print it.';
    starter = 'fruits = {\"apple\", \"banana\"}\n# Add \"kiwi\"\n';
    solution = 'fruits = {"apple", "banana"}\nfruits.add("kiwi")\nprint(fruits)';
    tags = ['sets'];
    return finish();
  }

  if (lower.includes('dict')) {
    content += 'Dictionaries map keys to values for fast lookup.\n';
    analogy = 'Analogy: a dictionary is an address book; names (keys) point to phone numbers (values).';
    example = 'person = {"name": "Ava", "age": 30}\nprint(person["name"])';
    walkthrough = ['Access values by key.'];
    prompt = 'Create a dictionary for a book with keys "title" and "pages".';
    starter = '# Create a dictionary called book with keys title and pages\n';
    solution = 'book = {"title": "Dune", "pages": 412}\nprint(book["title"])';
    tags = ['dictionaries'];
    return finish();
  }

  if (lower.includes('if') || lower.includes('elif') || lower.includes('else')) {
    content += 'Conditionals let your program choose a path based on a boolean test.\n';
    analogy = 'Analogy: a conditional is a fork in the road; the condition decides the route.';
    example = 'score = 82\nif score >= 90:\n    print("A")\nelif score >= 80:\n    print("B")\nelse:\n    print("C")';
    walkthrough = ['Test the first condition.', 'Use elif for the next check.', 'Use else as the fallback.'];
    prompt = 'Print "warm" if temp > 70 else print "cool".';
    starter = 'temp = 65\n# Use an if/else to print warm or cool\n';
    solution = 'temp = 65\nif temp > 70:\n    print("warm")\nelse:\n    print("cool")';
    tags = ['conditionals'];
    return finish();
  }

  if (lower.includes('loop') || lower.includes('while') || lower.includes('for')) {
    content += 'Loops repeat work. Use for when you know the range, while when you loop until a condition changes.\n';
    analogy = 'Analogy: a loop is a conveyor belt that keeps moving items until you stop it.';
    example = 'total = 0\nfor i in range(1, 4):\n    total += i\nprint(total)';
    walkthrough = ['Start total at 0.', 'Add each number.', 'Print the result.'];
    prompt = 'Use a while loop to count from 1 to 3.';
    starter = 'n = 1\n# Use a while loop to print 1, 2, 3\n';
    solution = 'n = 1\nwhile n <= 3:\n    print(n)\n    n += 1';
    tags = ['loops'];
    return finish();
  }

  if (lower.includes('function') || lower.includes('lambda')) {
    content += 'Functions package reusable logic. They take inputs (parameters) and return outputs.\n';
    analogy = 'Analogy: a function is a vending machine; inputs go in, outputs come out.';
    example = 'def add(a, b):\n    return a + b\n\nprint(add(2, 3))';
    walkthrough = ['Define the function with def.', 'Return a value.', 'Call the function.'];
    prompt = 'Write a function double(x) that returns x * 2.';
    starter = 'def double(x):\n    # return x * 2\n    ...\n\nprint(double(4))';
    solution = 'def double(x):\n    return x * 2\n\nprint(double(4))';
    tags = ['functions'];
    return finish();
  }

  if (lower.includes('__init__') || lower.includes('init method')) {
    content += '__init__ runs when you create an object, so it is used to set up initial state.\n';
    analogy = 'Analogy: __init__ is the setup checklist when you move into a new apartment.';
    example = 'class User:\n    def __init__(self, name, role):\n        self.name = name\n        self.role = role\n\nu = User("Ava", "admin")\nprint(u.name, u.role)';
    walkthrough = ['Define __init__ with parameters.', 'Assign to self.', 'Create the object with arguments.'];
    prompt = 'Create a class Book that stores title and pages in __init__.';
    starter = 'class Book:\n    def __init__(self, title, pages):\n        # store title and pages on self\n        ...\n\nb = Book("Dune", 412)\nprint(b.title, b.pages)';
    solution = 'class Book:\n    def __init__(self, title, pages):\n        self.title = title\n        self.pages = pages\n\nb = Book("Dune", 412)\nprint(b.title, b.pages)';
    tags = ['classes', 'init'];
    return finish();
  }

  if (lower.includes('class properties') || lower.includes('class property') || lower.includes('class attributes')) {
    content += 'Class properties (attributes) store data on each object.\n';
    analogy = 'Analogy: attributes are sticky notes attached to each object.';
    example = 'class Bike:\n    def __init__(self, gear):\n        self.gear = gear\n\nbike = Bike(3)\nprint(bike.gear)\nbike.gear = 5\nprint(bike.gear)';
    walkthrough = ['Create an attribute in __init__.', 'Read it with dot notation.', 'Update it directly.'];
    prompt = 'Create a class Team with a name attribute and print it.';
    starter = 'class Team:\n    def __init__(self, name):\n        self.name = name\n\nteam = Team("Lions")\n# Print the name\n';
    solution = 'class Team:\n    def __init__(self, name):\n        self.name = name\n\nteam = Team("Lions")\nprint(team.name)';
    tags = ['classes', 'attributes'];
    return finish();
  }

  if (lower.includes('class methods') || lower.includes('class method') || lower.includes('classmethod')) {
    content += 'Methods are functions that live on a class and act on its data.\n';
    analogy = 'Analogy: a method is a button on a device; pressing it changes the device state.';
    example = 'class Timer:\n    def __init__(self):\n        self.ticks = 0\n\n    def tick(self):\n        self.ticks += 1\n\n    def report(self):\n        return self.ticks\n\nt = Timer()\nt.tick()\nprint(t.report())';
    walkthrough = ['Define methods with self.', 'Change attributes inside the method.', 'Call the method on the object.'];
    prompt = 'Add a method add_point() that increments score by 1.';
    starter = 'class Scoreboard:\n    def __init__(self):\n        self.score = 0\n\n    def add_point(self):\n        # increase score by 1\n        ...\n\ns = Scoreboard()\ns.add_point()\nprint(s.score)';
    solution = 'class Scoreboard:\n    def __init__(self):\n        self.score = 0\n\n    def add_point(self):\n        self.score += 1\n\ns = Scoreboard()\ns.add_point()\nprint(s.score)';
    tags = ['classes', 'methods'];
    return finish();
  }

  if (lower.includes('inherit')) {
    content += 'Inheritance lets a new class reuse behavior from an existing class.\n';
    analogy = 'Analogy: inheritance is a recipe you copy and then tweak for a new dish.';
    example = 'class Animal:\n    def speak(self):\n        return "..." \n\nclass Dog(Animal):\n    def speak(self):\n        return "woof"\n\nprint(Dog().speak())';
    walkthrough = ['Create a base class.', 'Subclass it with class Child(Parent).', 'Override methods if needed.'];
    prompt = 'Create a class Car that inherits Vehicle and overrides sound().';
    starter = 'class Vehicle:\n    def sound(self):\n        return "hum"\n\nclass Car(Vehicle):\n    # Override sound to return "vroom"\n    ...\n\nprint(Car().sound())';
    solution = 'class Vehicle:\n    def sound(self):\n        return "hum"\n\nclass Car(Vehicle):\n    def sound(self):\n        return "vroom"\n\nprint(Car().sound())';
    tags = ['classes', 'inheritance'];
    return finish();
  }

  if (lower.includes('polymorph')) {
    content += 'Polymorphism means different objects can share the same interface.\n';
    analogy = 'Analogy: different tools can all have a handle; you hold each the same way.';
    example = 'class Cat:\n    def speak(self):\n        return "meow"\n\nclass Dog:\n    def speak(self):\n        return "woof"\n\nfor pet in [Cat(), Dog()]:\n    print(pet.speak())';
    walkthrough = ['Define the same method name on different classes.', 'Call the method in a shared loop.'];
    prompt = 'Create two classes that each implement size() and call them in a list.';
    starter = 'class Box:\n    def size(self):\n        return "small"\n\nclass Bag:\n    def size(self):\n        return "large"\n\nitems = [Box(), Bag()]\n# Print size() for each item\n';
    solution = 'class Box:\n    def size(self):\n        return "small"\n\nclass Bag:\n    def size(self):\n        return "large"\n\nitems = [Box(), Bag()]\nfor item in items:\n    print(item.size())';
    tags = ['classes', 'polymorphism'];
    return finish();
  }

  if (lower.includes('inner class')) {
    content += 'An inner class is defined inside another class and is scoped to it.\n';
    analogy = 'Analogy: an inner class is a small tool stored inside a bigger tool case.';
    example = 'class Outer:\n    class Inner:\n        def label(self):\n            return "inside"\n\ninner = Outer.Inner()\nprint(inner.label())';
    walkthrough = ['Define a class inside another class.', 'Access it with Outer.Inner.', 'Create an instance and call a method.'];
    prompt = 'Define an inner class Note inside Notebook that returns "note".';
    starter = 'class Notebook:\n    class Note:\n        def text(self):\n            return "note"\n\nn = Notebook.Note()\n# Print the text\n';
    solution = 'class Notebook:\n    class Note:\n        def text(self):\n            return "note"\n\nn = Notebook.Note()\nprint(n.text())';
    tags = ['classes', 'inner-classes'];
    return finish();
  }

  if (trimmed === 'python oop' || trimmed.endsWith(' oop') || trimmed.includes(' object oriented')) {
    content += 'Object-oriented programming (OOP) groups data and behavior together.\n';
    analogy = 'Analogy: OOP is a toolbox where each tool has both parts (data) and actions (methods).';
    example = 'class Counter:\n    def __init__(self):\n        self.value = 0\n\n    def bump(self):\n        self.value += 1\n\nc = Counter()\nc.bump()\nprint(c.value)';
    walkthrough = ['Create a class with data and behavior.', 'Make an object.', 'Call a method and observe state change.'];
    prompt = 'Create a class Lamp with a state (on/off) and a toggle() method.';
    starter = 'class Lamp:\n    def __init__(self):\n        self.on = False\n\n    def toggle(self):\n        # Flip the on/off state\n        ...\n\nlamp = Lamp()\nlamp.toggle()\nprint(lamp.on)';
    solution = 'class Lamp:\n    def __init__(self):\n        self.on = False\n\n    def toggle(self):\n        self.on = not self.on\n\nlamp = Lamp()\nlamp.toggle()\nprint(lamp.on)';
    tags = ['oop', 'classes'];
    return finish();
  }

  if (lower.includes('class') || lower.includes('object')) {
    content += 'Classes define new types with data (attributes) and behavior (methods).\n';
    analogy = 'Analogy: a class is a blueprint; objects are the houses built from it.';
    example = 'class Dog:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        return f\"{self.name} says woof\"\n\nd = Dog(\"Rex\")\nprint(d.speak())';
    walkthrough = ['Define __init__ to set up attributes.', 'Define methods for behavior.', 'Create an object and call a method.'];
    prompt = 'Create a class Car with attribute model and method label() that returns the model.';
    starter = 'class Car:\n    def __init__(self, model):\n        self.model = model\n\n    def label(self):\n        # return the model\n        ...\n\nc = Car(\"Civic\")\nprint(c.label())';
    solution = 'class Car:\n    def __init__(self, model):\n        self.model = model\n\n    def label(self):\n        return self.model\n\nc = Car(\"Civic\")\nprint(c.label())';
    tags = ['classes'];
    return finish();
  }

  if (lower.includes('module') || lower.includes('package') || lower.includes('import')) {
    content += 'Modules organize reusable code. You import them to access functions and data.\n';
    analogy = 'Analogy: modules are toolboxes; import brings the tools into your workspace.';
    example = 'import math\nprint(math.sqrt(81))';
    walkthrough = ['Import a module.', 'Use a function from that module.'];
    prompt = 'Import random and print a random integer from 1 to 6.';
    starter = 'import random\n# Print a random integer from 1 to 6\n';
    solution = 'import random\nprint(random.randint(1, 6))';
    tags = ['modules'];
    return finish();
  }

  if (lower.includes('file')) {
    content += 'File handling lets you read and write data stored on disk.\n';
    analogy = 'Analogy: a file is a notebook; open it, write in it, and close it.';
    example = 'with open("notes.txt", "w") as f:\n    f.write("hello")\n\nwith open("notes.txt", "r") as f:\n    print(f.read())';
    walkthrough = ['Use with open() to manage files safely.', 'Write then read the file.'];
    prompt = 'Write the word "ok" to a file called "log.txt".';
    starter = '# Open log.txt in write mode and write "ok"\n';
    solution = 'with open("log.txt", "w") as f:\n    f.write("ok")';
    tags = ['files'];
    return finish();
  }

  if (lower.includes('exception') || lower.includes('try')) {
    content += 'Exceptions handle errors gracefully instead of crashing your program.\n';
    analogy = 'Analogy: exceptions are airbags that deploy when something goes wrong.';
    example = 'try:\n    value = int("abc")\nexcept ValueError:\n    print("Not a number")';
    walkthrough = ['Wrap risky code in try.', 'Catch errors in except.'];
    prompt = 'Catch ZeroDivisionError when dividing by zero.';
    starter = '# Use try/except to catch ZeroDivisionError\n';
    solution = 'try:\n    1 / 0\nexcept ZeroDivisionError:\n    print("bad")';
    tags = ['errors'];
    return finish();
  }

  if (lower.includes('regex')) {
    content += 'Regular expressions match text patterns for search and validation.\n';
    analogy = 'Analogy: regex is a metal detector that beeps for specific patterns.';
    example = 'import re\ntext = "catnap"\nprint(bool(re.search("cat", text)))';
    walkthrough = ['Use re.search() to find a pattern.'];
    prompt = 'Check if "dog" appears in "hotdog".';
    starter = 'import re\ntext = "hotdog"\n# Print True if dog is found\n';
    solution = 'import re\ntext = "hotdog"\nprint(bool(re.search("dog", text)))';
    tags = ['regex'];
    return finish();
  }

  if (lower.includes('json')) {
    content += 'JSON stores structured data. The json module converts between JSON text and Python objects.\n';
    analogy = 'Analogy: JSON is a shipping label for data; json.loads reads it into Python.';
    example = 'import json\npayload = "{\\"x\\": 1}"\nprint(json.loads(payload)["x"])';
    walkthrough = ['Use json.loads to parse.', 'Access values by key.'];
    prompt = 'Parse {"name": "Ava"} and print the name.';
    starter = 'import json\njson_text = \"{\\\"name\\\": \\\"Ava\\\"}\"\\n# Print the name\n';
    solution = 'import json\njson_text = "{\\"name\\": \\"Ava\\"}"\nprint(json.loads(json_text)["name"])';
    tags = ['json'];
    return finish();
  }

  if (lower.includes('date') || lower.includes('time')) {
    content += 'Datetime tools help you work with dates and times for schedules and timestamps.\n';
    analogy = 'Analogy: datetime is a calendar plus a clock inside your code.';
    example = 'from datetime import date\nprint(date.today())';
    walkthrough = ['Import date from datetime.', 'Call date.today().'];
    prompt = 'Print today\'s date.';
    starter = 'from datetime import date\n# Print today\n';
    solution = 'from datetime import date\nprint(date.today())';
    tags = ['datetime'];
    return finish();
  }

  if (lower.includes('math')) {
    content += 'The math module provides numeric utilities like square roots and rounding.\n';
    analogy = 'Analogy: math is a calculator you can call from code.';
    example = 'import math\nprint(math.sqrt(49))';
    walkthrough = ['Import math.', 'Call math.sqrt.'];
    prompt = 'Compute the square root of 81.';
    starter = 'import math\n# Print the square root of 81\n';
    solution = 'import math\nprint(math.sqrt(81))';
    tags = ['math'];
    return finish();
  }

  content += 'This topic expands core Python knowledge with a focused example.\n';
  analogy = 'Analogy: each concept is a tool; the more tools you have, the more problems you can solve.';
  example = 'print("Hello, Python")';
  walkthrough = ['Run the example and confirm the output.'];
  prompt = 'Print a greeting of your choice.';
  starter = '# Print a greeting\n';
  solution = 'print("Hello, Python")';
  tags = ['basics'];
  return finish();
};

const sqlTemplate = (title) => {
  const lower = normalizeTitle(title);
  let content = `# ${title}\n\n## Big idea\n`;
  let analogy = '';
  let example = '';
  let walkthrough = [];
  let prompt = '';
  let starter = '';
  let solution = '';
  let tags = [];

  const finish = () => {
    content += `${analogy ? `${analogy}\n\n` : ''}`;
    content += `## Example\n\`\`\`sql\n${example}\n\`\`\`\n\n`;
    if (walkthrough.length) {
      content += `## Walkthrough\n${walkthrough.map((s, i) => `${i + 1}. ${s}`).join('\n')}\n\n`;
    }
    content += `## Your turn\n${prompt}\n`;
    return { content, starter, solution, tags };
  };

  if (lower.includes('join')) {
    content += 'Joins combine rows from multiple tables by matching keys.\n';
    analogy = 'Analogy: a join is a zipper that aligns rows using shared keys.';
    example = 'SELECT c.name, o.id\nFROM customers c\nJOIN orders o ON c.id = o.customer_id;';
    walkthrough = ['Pick the left table and right table.', 'Choose a shared key.', 'Join and select the columns you need.'];
    prompt = 'Join customers to orders and return customer name + order id.';
    starter = 'SELECT c.name, o.id\nFROM customers c\nJOIN orders o ON c.id = o.customer_id;';
    solution = starter;
    tags = ['join'];
    return finish();
  }

  if (lower.includes('group by') || lower.includes('aggregate') || lower.includes('count') || lower.includes('sum') || lower.includes('avg') || lower.includes('min') || lower.includes('max')) {
    content += 'Aggregations summarize groups of rows into metrics.\n';
    analogy = 'Analogy: grouping is sorting receipts into piles and summing each pile.';
    example = 'SELECT status, COUNT(*) AS total\nFROM orders\nGROUP BY status;';
    walkthrough = ['Choose a grouping column.', 'Apply an aggregate like COUNT, SUM, or AVG.'];
    prompt = 'Count orders by status.';
    starter = 'SELECT status, COUNT(*) AS total\nFROM orders\nGROUP BY status;';
    solution = starter;
    tags = ['aggregates'];
    return finish();
  }

  if (lower.includes('having')) {
    content += 'HAVING filters groups after aggregation, unlike WHERE which filters rows first.\n';
    analogy = 'Analogy: HAVING is a quality check after grouping, while WHERE is a gate before grouping.';
    example = 'SELECT customer_id, COUNT(*) AS total\nFROM orders\nGROUP BY customer_id\nHAVING COUNT(*) > 5;';
    walkthrough = ['Group rows.', 'Apply HAVING to keep only large groups.'];
    prompt = 'Keep only customers with more than 5 orders.';
    starter = 'SELECT customer_id, COUNT(*) AS total\nFROM orders\nGROUP BY customer_id\nHAVING COUNT(*) > 5;';
    solution = starter;
    tags = ['having'];
    return finish();
  }

  if (lower.includes('where') || lower.includes('and') || lower.includes('or') || lower.includes('not') || lower.includes('between') || lower.includes('like') || lower.includes('in') || lower.includes('wildcard')) {
    content += 'WHERE filters rows based on conditions.\n';
    analogy = 'Analogy: WHERE is a sieve that lets only matching rows pass.';
    example = 'SELECT *\nFROM flights\nWHERE month = 1 AND day = 1;';
    walkthrough = ['Start with SELECT * FROM table.', 'Add a condition with WHERE.', 'Combine conditions with AND/OR.'];
    prompt = 'Filter orders where status = "shipped".';
    starter = 'SELECT *\nFROM orders\nWHERE status = "shipped";';
    solution = starter;
    tags = ['where'];
    return finish();
  }

  if (lower.includes('order by') || lower.includes('top') || lower.includes('limit')) {
    content += 'ORDER BY sorts rows; LIMIT (or TOP) restricts the output size.\n';
    analogy = 'Analogy: sorting is lining up books; limit is grabbing only the first few.';
    example = 'SELECT *\nFROM orders\nORDER BY total DESC\nLIMIT 5;';
    walkthrough = ['Sort by the column you care about.', 'Limit to the first N rows.'];
    prompt = 'Return the top 3 orders by total.';
    starter = 'SELECT *\nFROM orders\nORDER BY total DESC\nLIMIT 3;';
    solution = starter;
    tags = ['order_by'];
    return finish();
  }

  if (lower.includes('distinct')) {
    content += 'DISTINCT removes duplicates from a column or set of columns.\n';
    analogy = 'Analogy: DISTINCT is like removing duplicate names from a guest list.';
    example = 'SELECT DISTINCT department\nFROM employees;';
    walkthrough = ['Use DISTINCT after SELECT.', 'List the column(s) to dedupe.'];
    prompt = 'List unique departments.';
    starter = 'SELECT DISTINCT department\nFROM employees;';
    solution = starter;
    tags = ['distinct'];
    return finish();
  }

  if (lower.includes('insert')) {
    content += 'INSERT adds new rows to a table. It is a DML command that changes data, not structure.\n';
    analogy = 'Analogy: INSERT is adding a new row to a spreadsheet.';
    example = 'INSERT INTO products (name, price)\nVALUES ("Widget", 25.00);';
    walkthrough = ['Name the table.', 'List columns.', 'Provide values in the same order.'];
    prompt = 'Insert a product named "Gizmo" priced at 19.99.';
    starter = 'INSERT INTO products (name, price)\nVALUES ("Gizmo", 19.99);';
    solution = starter;
    tags = ['insert'];
    return finish();
  }

  if (lower.includes('update')) {
    content += 'UPDATE modifies existing rows. Use WHERE to avoid changing everything.\n';
    analogy = 'Analogy: UPDATE is editing a cell in a spreadsheet.';
    example = 'UPDATE products\nSET price = 30\nWHERE id = 1;';
    walkthrough = ['Choose the table.', 'Set new values.', 'Use WHERE to limit rows.'];
    prompt = 'Update order 1001 to status "shipped".';
    starter = 'UPDATE orders\nSET status = "shipped"\nWHERE id = 1001;';
    solution = starter;
    tags = ['update'];
    return finish();
  }

  if (lower.includes('delete')) {
    content += 'DELETE removes rows from a table. Always add WHERE unless you truly mean all rows.\n';
    analogy = 'Analogy: DELETE is erasing rows from a spreadsheet.';
    example = 'DELETE FROM orders\nWHERE status = "cancelled";';
    walkthrough = ['Specify the table.', 'Use WHERE to target rows.'];
    prompt = 'Delete rows where status = "expired".';
    starter = 'DELETE FROM orders\nWHERE status = "expired";';
    solution = starter;
    tags = ['delete'];
    return finish();
  }

  if (lower.includes('create table') || lower.includes('alter table') || lower.includes('drop table') || lower.includes('constraint') || lower.includes('primary key') || lower.includes('foreign key') || lower.includes('index')) {
    content += 'DDL statements define or change the database structure, while DML changes the data inside tables.\n';
    analogy = 'Analogy: DDL is the blueprint and renovation plan for your database.';
    if (lower.includes('create table')) {
      example = 'CREATE TABLE customers (\n  id INT PRIMARY KEY,\n  name TEXT NOT NULL,\n  email TEXT UNIQUE\n);';
      walkthrough = ['Pick a table name.', 'Define columns and types.', 'Add constraints for data integrity.'];
      prompt = 'Create a table called orders with id (INT) and total (DECIMAL).';
      starter = 'CREATE TABLE orders (\n  id INT,\n  total DECIMAL(10,2)\n);';
      solution = starter;
    } else if (lower.includes('alter table')) {
      example = 'ALTER TABLE customers\nADD COLUMN city TEXT;';
      walkthrough = ['Alter the table.', 'Add or modify columns.'];
      prompt = 'Add a column named status to orders.';
      starter = 'ALTER TABLE orders\nADD COLUMN status TEXT;';
      solution = starter;
    } else if (lower.includes('drop table')) {
      example = 'DROP TABLE old_data;';
      walkthrough = ['Be sure you no longer need the table.', 'Drop it explicitly.'];
      prompt = 'Drop a table named temp_data.';
      starter = 'DROP TABLE temp_data;';
      solution = starter;
    } else if (lower.includes('foreign key')) {
      example = 'CREATE TABLE orders (\n  id INT PRIMARY KEY,\n  customer_id INT,\n  FOREIGN KEY (customer_id) REFERENCES customers(id)\n);';
      walkthrough = ['Create a key in child table.', 'Reference the parent table.'];
      prompt = 'Add a foreign key from orders.customer_id to customers.id.';
      starter = 'CREATE TABLE orders (\n  id INT PRIMARY KEY,\n  customer_id INT,\n  FOREIGN KEY (customer_id) REFERENCES customers(id)\n);';
      solution = starter;
    } else if (lower.includes('index')) {
      example = 'CREATE INDEX idx_users_email ON users(email);';
      walkthrough = ['Pick the table and column to speed up.'];
      prompt = 'Create an index on orders(order_date).';
      starter = 'CREATE INDEX idx_orders_date ON orders(order_date);';
      solution = starter;
    } else {
      example = 'ALTER TABLE customers\nADD CONSTRAINT chk_age CHECK (age >= 0);';
      walkthrough = ['Use constraints to enforce data rules.'];
      prompt = 'Add a NOT NULL constraint to users.email (syntax shown in example).';
      starter = 'ALTER TABLE users\nALTER COLUMN email SET NOT NULL;';
      solution = starter;
    }
    tags = ['schema'];
    return finish();
  }

  if (lower.includes('null')) {
    content += 'NULL represents missing or unknown values.\n';
    analogy = 'Analogy: NULL is an empty box, not a value like 0 or "". ';
    example = 'SELECT *\nFROM users\nWHERE email IS NULL;';
    walkthrough = ['Use IS NULL or IS NOT NULL to test for missing values.'];
    prompt = 'Select rows where phone IS NOT NULL.';
    starter = 'SELECT *\nFROM users\nWHERE phone IS NOT NULL;';
    solution = starter;
    tags = ['nulls'];
    return finish();
  }

  if (lower.includes('case')) {
    content += 'CASE adds conditional logic inside a query.\n';
    analogy = 'Analogy: CASE is a built-in if/else for SQL rows.';
    example = 'SELECT amount,\n  CASE WHEN amount > 100 THEN "high" ELSE "low" END AS bucket\nFROM payments;';
    walkthrough = ['Write WHEN conditions in order.', 'Add ELSE for fallback.'];
    prompt = 'Create a bucket column for orders > 500 labeled "big".';
    starter = 'SELECT total,\n  CASE WHEN total > 500 THEN "big" ELSE "small" END AS bucket\nFROM orders;';
    solution = starter;
    tags = ['case'];
    return finish();
  }

  if (lower.includes('union') || lower.includes('intersect') || lower.includes('except')) {
    content += 'Set operators combine results from multiple queries.\n';
    analogy = 'Analogy: UNION is stacking lists; INTERSECT is the overlap; EXCEPT is subtraction.';
    example = 'SELECT name FROM customers\nUNION\nSELECT name FROM leads;';
    walkthrough = ['Write two SELECT statements with matching columns.', 'Use the set operator between them.'];
    prompt = 'Union active_customers with prospects (name column).';
    starter = 'SELECT name FROM active_customers\nUNION\nSELECT name FROM prospects;';
    solution = starter;
    tags = ['set_ops'];
    return finish();
  }

  content += 'This topic expands core SQL knowledge with a focused example.\n';
  analogy = 'Analogy: each SQL clause is a tool in a query toolbox.';
  example = 'SELECT * FROM example_table;';
  walkthrough = ['Run the example and confirm the output shape.'];
  prompt = 'Write a simple SELECT from any table.';
  starter = 'SELECT * FROM example_table;';
  solution = starter;
  tags = ['sql_basics'];
  return finish();
};

const updateLessons = (course, chapterId, templateFn) => {
  const ids = getChapterLessonIds(course, chapterId);
  let updated = 0;
  ids.forEach((id) => {
    const lesson = lessons[id];
    if (!lesson) return;
    const { content, starter, solution, tags } = templateFn(lesson.title);
    lesson.content = content;
    lesson.starter_code = starter;
    lesson.solution_code = solution;
    if (Array.isArray(tags) && tags.length) {
      lesson.concept_tags = tags;
    }
    lesson.interaction_confidence = 1;
    lesson.manual_review = false;
    updated += 1;
  });
  return updated;
};

const pythonUpdated = updateLessons(pythonCourse, 150, pythonTemplate);
const sqlUpdated = updateLessons(sqlCourse, 215, sqlTemplate);

fs.writeFileSync(lessonsPath, JSON.stringify(lessons, null, 2));

const report = {
  python_updated: pythonUpdated,
  sql_updated: sqlUpdated
};

fs.writeFileSync(path.resolve(__dirname, './w3schools_template_upgrade_report.json'), JSON.stringify(report, null, 2));
console.log(`Upgraded ${pythonUpdated} Python lessons and ${sqlUpdated} SQL lessons.`);
