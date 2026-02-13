# Design Patterns Theory
In this document the design patterns observer and decorator are described. <br>
Source: https://refactoring.guru/design-patterns/catalog

## Pattern: Observer
The Observer pattern is a behavioral design pattern that helps objects communicate when something changes. 
It solves the problem of keeping multiple parts of a program updated without connecting them too tightly. 
In many applications, one object contains important data, and several other objects depend on that data. 
If each dependent object had to constantly check for updates on its own, the system would become inefficient and complicated. <br>

The Observer pattern introduces a simple subscription system. One main object, called the subject, keeps a list of observers. 
These observers are objects that want to be informed when the subject changes. Whenever the subject’s state is updated, it automatically sends a notification to all observers. 
Each observer then decides how to respond, for example by updating a display or recalculating information. <br>

The main idea behind this pattern is to separate responsibilities. The subject only manages its data and notifications, while observers handle their own reactions. 
Because of this separation, new observers can be added or removed without changing the subject itself. This makes the system more flexible and easier to maintain. <br>

A simple way to understand this pattern is to compare it to everyday subscription systems. For example, when someone subscribes to a newsletter or follows a social media channel, 
they automatically receive updates whenever new content is published. The subscriber chooses what they want to follow and is notified without having to manually check for changes. 
In this comparison, the subscriber acts like the observer, while the newsletter or channel represents the subject. 
This illustrates how the Observer pattern allows interested parties to stay informed efficiently while remaining independent.


## Pattern: Decorator
The Decorator pattern is a structural design pattern that makes it possible to extend an object’s behavior without directly modifying its original code. It is useful when software components need additional features, but changing the base implementation would make the system harder to maintain. Creating many subclasses for every variation can also lead to unnecessary complexity and reduce clarity. <br>

Instead of altering the original object, the Decorator pattern adds functionality by placing another object around it. This outer object provides extra behavior while still supporting the same interface as the wrapped object. Because both objects follow the same structure, they can be used interchangeably. Several decorators can be combined to gradually build more advanced behavior, with each decorator contributing a specific feature. <br>

The core idea is to keep the original object focused on its main responsibility while allowing enhancements to be added when required. This approach improves flexibility, since new features can be introduced without rewriting existing components. It also helps maintain clean and organized code, because responsibilities remain separated.<br>

A practical way to imagine this pattern is customizing a basic product. For example, a plain coffee can be enhanced with milk, syrup, or whipped cream. The base drink stays the same, but each addition changes the final result. In the same way, decorators add optional behavior to an object without replacing its original purpose.
