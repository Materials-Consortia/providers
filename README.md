# OPTiMaDe Providers Index Meta-Database

This repository hosts the providers.json file for OPTiMaDe that lists reserved database-specific prefixes and URLs to the index databases of all database providers that participate in the OPTiMaDe network.

The repository is published in form of a statically hosted OPTiMaDe Index Meta-Database here:

- https://www.optimade.org/providers/

If you seek specifically the current contents of the providers.json file for the latest version of the OPTiMaDe specification, you can access it using this URL:

- https://www.optimade.org/providers/links/

If you seek the current contents of the providers.json file for any older version of the OPTiMaDe specification, you can access it using this URL:

- https://www.optimade.org/providers/*<version>*/links/


## Repository organization

The OPTiMaDe providers repository is hosted here: https://github.com/Materials-Consortia/providers

The paths are organized this way:

- `src/<version>/providers.json` is the current providers.json file formatted according to OPTiMaDe version `<version>`.

- `info` and `links` are symbolic links into the subdirectory matching the latest release of the OPTiMaDe specification.

- `<version>`: every released version of the OPTiMaDe specification gets a subdirectory organized to confirm with the URLs as defined for an OPTiMaDe base url. The `<version>/links/index.html` is a symbolic link to `src/<version>/providers.json`.

To update the list of providers, please file a pull-request against the repository.
A PR MUST update ALL provider.json files `src/<version>/providers.json`.
This updates the current list of providers for implementations of all versions of the OPTiMaDe protocol.
