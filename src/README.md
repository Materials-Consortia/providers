This directory contains the source static files used to serve the info and links endpoints for the providers index meta-database.

There shall be only one copy of these files for every non-compatible version of their format.
Hence, they are stored in the directories:
- links/\<version>\/providers.json
- info/\<version>\/info.json
where <version> is the *first* version where a new format has been introduced, starting with v1.

The providers index meta-database is served from the root of the repository.
The root directory contains one subdirectory per major version of the specification, in which the links and info endpoints point into these versioned directories.
