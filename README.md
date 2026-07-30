# UBFlex
 
**UBFlex** is the interoperability reference for building flexibility within
the BlueBird project.
 
This repository provides a common entry point to the BlueBird components that
support the connection between building-level flexibility, market information
and Knowledge Engine-based integrations.
 
> UBFlex does not replace the internal responsibilities of BlueBird
> components. It provides the common context in which they can be integrated
> consistently.
 
## Purpose
 
Energy flexibility involves several technical domains: local building control,
forecasting and optimisation, market information, and system-to-system data
exchange. UBFlex provides a shared project-level reference for documenting and
aligning these integrations.
 
The objectives of this repository are to:
 
- Explain the role of UBFlex in the BlueBird ecosystem
- Provide a single navigation point to the main related components
- Record UBFlex-related documentation, decisions and compatibility information
- Make the relationship between component repositories visible to users, developers and project stakeholders
 
## BlueBird components
 
| Component | Role in the UBFlex ecosystem | Repository |
|---|---|---|
| Flexibility Manager (FM) | Performs local flexibility assessment, optimisation and control for building assets | [flexibility-manager](https://github.com/BlueBird-project/flexibility-manager) |
| Trading Manager (TM) | Provides market-related information and supports the market-facing integration of flexibility services | [trading-manager](https://github.com/BlueBird-project/trading-manager) |
| KE PyClient | Python client library for technical integrations with the TNO Knowledge Engine | [ke-pyclient](https://github.com/BlueBird-project/ke-pyclient) |
 
## Conceptual view
 
```text
Building assets and Building Management Systems
                    |
                    v
         Flexibility Manager (FM)
                    |
                    |  UBFlex ecosystem
                    |
                    v
           Trading Manager (TM)
                    |
                    v
        Energy markets and grid services
 
KE PyClient supports Knowledge Engine-based integrations
used by relevant BlueBird components.
```
 
The exact interfaces, data mappings and transport mechanisms are maintained in
the corresponding component repositories. This repository does not duplicate
their technical documentation.
 
## Current status
 
UBFlex is an evolving BlueBird integration reference.
 
The components linked above may be at different stages of implementation and
may expose different interfaces depending on the pilot, deployment environment
or software version. An interface should only be described as UBFlex-compliant
when its applicable UBFlex profile, version and implementation status have
been explicitly documented.
 
## Related resources
 
- [BlueBird project website](https://bluebird-project.eu/)
- [Flexibility Manager repository](https://github.com/BlueBird-project/flexibility-manager)
- [Trading Manager repository](https://github.com/BlueBird-project/trading-manager)
- [KE PyClient repository](https://github.com/BlueBird-project/ke-pyclient)
 
## Contributing
 
Changes to this repository should focus on documentation that is shared across BlueBird components.
 
Component-specific implementation details, deployment instructions and API documentation should remain in the relevant component repository. Cross-cutting changes affecting multiple components should be discussed and agreed with the relevant BlueBird technical owners before publication.
