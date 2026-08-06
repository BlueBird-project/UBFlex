**UBFlex** is the BlueBird common interface for interoperability between
building-flexibility services and connected external systems.

It brings together the BlueBird-specific semantic and technical assets needed
to configure and use Knowledge Engine-based integrations consistently across
the project.

UBFlex is built around the following elements:

- The TNO Knowledge Engine (KE)
- KE Smart Connectors (SC)
- BlueBird graph-pattern configurations
- BlueBird ontology definitions
- Deployment and integration configuration
- Documentation and examples for connected BlueBird components

## Purpose

UBFlex provides the common integration layer used by relevant BlueBird
components to exchange information in a consistent way.

It does not replace the domain logic of those components:

- The **Flexibility Manager** remains responsible for local flexibility
  assessment, optimisation and control.
- The **Trading Manager** remains responsible for market-related information
  and trading functionality.
- **UBFlex** provides the shared interface assets used to configure and
  connect those components through Knowledge Engine-based interactions.

## Architecture

```text
+------------------------+       +------------------------+
| Flexibility Manager    |       | Trading Manager        |
|                        |       |                        |
| Local optimisation     |       | Market-related logic   |
| and control            |       | and negotiation        |
+-----------+------------+       +-----------+------------+
            |                                  |
            +---------------+------------------+
                            |
                            v
              +-----------------------------+
              |           UBFlex            |
              |                             |
              | BlueBird ontology           |
              | Graph patterns              |
              | Smart Connector config      |
              | KE deployment configuration |
              +--------------+--------------+
                             |
                             v
                  Knowledge Engine runtime
```

## Repository contents

| Directory | Contents |
|---|---|
| `ontology/` | BlueBird-specific ontology definitions and documentation |
| `graph-patterns/` | Graph-pattern configurations for the relevant KE Smart Connectors |
| `smart-connectors/` | Smart Connector configuration and integration resources |
| `compose/` | Docker or Docker Compose configuration, where applicable |
| `docs/` | Architecture, integration, compatibility and usage documentation |
| `examples/` | Validated examples of UBFlex integrations |

The repository contents will evolve as the relevant artefacts are agreed,
implemented and validated.

## Related repositories

| Component | Role | Repository |
|---|---|---|
| Flexibility Manager | Local flexibility optimisation and control | [flexibility-manager](https://github.com/BlueBird-project/flexibility-manager) |
| Trading Manager | Market-related information and trading functionality | [trading-manager](https://github.com/BlueBird-project/trading-manager) |
| KE PyClient | Generic Python client library for the TNO Knowledge Engine | [ke-pyclient](https://github.com/BlueBird-project/ke-pyclient) |

## KE PyClient dependency

UBFlex uses the Knowledge Engine and may use the
[KE PyClient](https://github.com/BlueBird-project/ke-pyclient) library for
Python-based integrations.

`ke-pyclient` is maintained as a separate repository. It is a reusable client
library and is not renamed or redistributed as part of UBFlex.

## Compatibility

The compatibility of UBFlex assets with the connected BlueBird components is
documented in [docs/compatibility.md](docs/compatibility.md).

Each validated UBFlex release should identify the compatible versions of:

- KE PyClient
- Flexibility Manager
- Trading Manager
- Knowledge Engine and Smart Connector runtime, where applicable

## Licensing and attribution

This repository contains BlueBird-specific integration assets. The licence,
copyright notices and attribution requirements of every imported or reused
asset must be preserved.

The TNO Knowledge Engine and the KE PyClient are maintained separately and
retain their respective licensing terms."
