# Bazaar CI

## Backend

### `bazaarci.runner`

A simple example, two steps where the first step produces a product `p` that is consumed by the second step.

```python
from bazaar.runner import Graph, Step

g = Graph("g")
s1 = Step(g, "Step1", target=lambda: print("Step1"))
s2 = Step(g, "Step2", target=lambda: print("Step2"))

s1.produces("p")  # Step 1 Produces "p"
s2.consumes("p")  # Step 2 Consumes "p"

g.start()  # Begin Thread Execution
```

## Frontend

### `bazaarci.web`

### `bazaarci.cli`
