# Piniverse

Piniverse is a simple library to programmatically orchestrate function calls for Python. 

Table of contents
---------------

- [Features Support](#features-support)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Limitations](#limitations)
- [Contributions](#contributions)

Features Support 
---------------

* Topological ordering and execution of all pinned functions inside a python package 

Prerequisites 
---------------

* Python 3.7

Getting Started
---------------

### Installation

```
$ pip install piniverse
```

### Basic Usage

Piniverse targets a package.

```
.
├── workspace/    <-- workspace directory
├── script.py     <-- script file

```

To orchestrate your functions, pin them! The ordering is defined by the concepts of tasks and towards.

```
# workspace/

from piniverse import Pinned


@Pinned(
  task='1',
  toward='2', 
  arguments={
    args: ['Hello World']
    kwargs: {'content': 'Programming exercise...'}
  }
)
def simple_print(title: str, content: str = '') -> None:
  message = """
    Title: {}
    Content: 
      {}
  """.format(title, content)
  
  print(message)


@Pinned(
  task='2',
  arguments={
    args: ['A pretty Hello World']
    kwargs: {'content': 'A pretty programming exercise!'
  }
)
def pretty_print(title: str, content: str = '') -> None:
  message = """
    Pretty Title: {}
    Pretty Content: 
      {}
  """.format(title, content)

```

To execute your package's functions, it is an easy 2-steps procedure: plan and apply.

```
# script.py

import piniverse
import workspace


piniverse.plan(workspace)
piniverse.apply()

```

### User Interface

Piniverse also provides a straightforward visualization of your task definitions.

```
TBD
```

Limitations 
---------------

Presently, Piniverse solely supports standalone functions.

Contributions 
---------------

Contributions are more than welcome! Check out the [contribution documentation](https://github.com/hzhao19/piniverse/blob/master/CONTRIBUTIONS.rst).
