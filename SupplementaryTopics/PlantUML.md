# PlantUML

PlantUML is a powerful tool that allows you to create various types of UML diagrams using simple textual descriptions. Here is an overview of the syntax for different types of UML diagrams:

## Class Diagram

**Syntax:**

```
@startuml
class ClassName {
  +attribute1: Type
  -attribute2: Type
  +method1(param1: Type): ReturnType
  -method2(param2: Type): ReturnType
}

ClassName1 --> ClassName2: Association
ClassName1 --|> ClassName3: Inheritance
ClassName1 ..> ClassName4: Dependency
ClassName1 o-- ClassName5: Aggregation
ClassName1 *-- ClassName6: Composition
@enduml
```



```plantuml
@startuml
class ClassName {
  +attribute1: Type
  -attribute2: Type
  +method1(param1: Type): ReturnType
  -method2(param2: Type): ReturnType
}

ClassName1 --> ClassName2: Association
ClassName1 --|> ClassName3: Inheritance
ClassName1 ..> ClassName4: Dependency
ClassName1 o-- ClassName5: Aggregation
ClassName1 *-- ClassName6: Composition
@enduml
```

**Explanation:**

- Define a class using the `class` keyword.
- Use `+` for public, `-` for private, and `#` for protected attributes and methods.
- Relationships: Association (`-->`), Inheritance (`--|>`), Dependency (`..>`), Aggregation (`o--`), Composition (`*--`).

## Object Diagram

**Syntax:**

```plantuml
@startuml
object ObjectName1 {
  attribute1 = value1
  attribute2 = value2
}

object ObjectName2 {
  attributeA = valueA
  attributeB = valueB
}

ObjectName1 --> ObjectName2: Association
@enduml
```

**Explanation:**

- Define objects using the `object` keyword.
- List attributes and their values within the object block.
- Relationships: Association (`-->`).

## Use Case Diagram

**Syntax:**

```plantuml
@startuml
actor ActorName

usecase "Use Case 1" as UC1
usecase "Use Case 2" as UC2

ActorName --> UC1
ActorName --> UC2

UC1 -right-> UC2 : <<include>>
UC1 .> UC3 : <<extend>>
@enduml
```

**Explanation:**

- Define actors using the `actor` keyword.
- Define use cases using the `usecase` keyword.
- Relationships: Association (`-->`), Include (`-right->` with `<<include>>`), Extend (`.>` with `<<extend>>`).

## Sequence Diagram

**Syntax:**

```plantuml
@startuml
actor User
participant "System" as System

User -> System: Request
System -> User: Response
System -> System: Internal call
@enduml
```

**Explanation:**

- Define actors and participants.
- Use `->` for synchronous messages, `-->` for asynchronous messages.
- Use `:` to label messages.

## Activity Diagram

**Syntax:**

```plantuml
@startuml
start
:Initial Action;
:Next Action;
if (Condition?) then (yes)
  :Action if true;
else (no)
  :Action if false;
endif
stop
@enduml
```

**Explanation:**

- Use `start` and `stop` for start and end points.
- Use `:` to define actions.
- Use `if` and `endif` for decision points.

## State Diagram

**Syntax:**

```plantuml
@startuml
[*] --> State1
State1 --> State2 : Event
State2 --> [*]
@enduml
```

**Explanation:**

- Use `[*]` for initial and final states.
- Define states and transitions using `-->`.

## Component Diagram

**Syntax:**

```plantuml
@startuml
component Component1 {
  [Interface1]
  [Interface2]
}

component Component2 {
  [Interface3]
}

Component1 --> Component2
@enduml
```

**Explanation:**

- Use `component` to define components.
- Use `[]` to define interfaces.
- Use `-->` to define relationships.

## Deployment Diagram

**Syntax:**

```plantuml
@startuml
node "Server" {
  artifact "WebApp.war"
}

node "Client" {
  artifact "ClientApp.exe"
}

Server --> Client
@enduml
```

**Explanation:**

- Use `node` to define nodes.
- Use `artifact` to define artifacts.
- Use `-->` to define relationships.

### Conclusion

PlantUML provides a flexible and easy-to-use syntax to create various UML diagrams. By defining actors, classes, use cases, objects, states, activities, components, and nodes using simple textual descriptions, you can effectively model the structure and behavior of your system.
