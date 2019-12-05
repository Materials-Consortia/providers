# OPTiMaDe Providers Index Meta-Database

The list of OPTiMaDe providers keeps track of all reserved database-specific prefixes and the URLs to the index databases of all OPTiMaDe database providers that participate in the [OPTiMaDe network](https://www.optimade.org/).

The list of providers is published in the form of a statically hosted OPTiMaDe Index Meta-Database here:

- [https://www.optimade.org/providers/](https://www.optimade.org/providers/)

If you specifically seek the current list of providers for the latest version of the OPTiMaDe specification, you can access it at this URL:

- [https://www.optimade.org/providers/links/](https://www.optimade.org/providers/links/)

If you seek the current list of providers for any older version of the OPTiMaDe specification, you can access it using this URL:

- [https://www.optimade.org/providers/*\<version\>*/links/](https://www.optimade.org/providers/<version>/links/)


## Repository organization

The OPTiMaDe providers repository is hosted here: [https://github.com/Materials-Consortia/providers](https://github.com/Materials-Consortia/providers)

The paths in the repository are organized this way:

- `src/<version>/providers.json` is the current providers.json file formatted according to OPTiMaDe version `<version>`.

- `info` and `links` are symbolic links into the subdirectory matching the latest release of the OPTiMaDe specification.

- `<version>`: every released version of the OPTiMaDe specification gets a subdirectory organized to confirm with the URLs as defined for an OPTiMaDe base url. The `<version>/links/index.html` is a symbolic link to `src/<version>/providers.json`.

To update the list of providers, please file a pull-request against the repository.
This pull-request MUST update ALL the provider.json files `src/<version>/providers.json`.
This way, the current list of providers is updated for implementations across all versions of the OPTiMaDe protocol.
