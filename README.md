# OPTiMaDe Providers Index Meta-Database

The list of OPTiMaDe providers keeps track of all reserved database-specific prefixes and the URLs to the index databases of all OPTiMaDe database providers that participate in the [OPTiMaDe network](https://www.optimade.org/).

The list of providers is published in the form of a statically hosted OPTiMaDe Index Meta-Database here:

- [https://www.optimade.org/providers/](https://www.optimade.org/providers/)

If you specifically seek the current list of providers for the latest version of the OPTiMaDe specification, you can access it at this URL:

- [https://www.optimade.org/providers/providers.json](https://www.optimade.org/providers/providers.json)

If you seek the current list of providers for any older version of the OPTiMaDe specification, you can access it using this URL:

- [https://www.optimade.org/providers/*\<version\>*/links](https://www.optimade.org/providers/<version>/links)


## Repository organization

The OPTiMaDe providers repository is hosted here: [https://github.com/Materials-Consortia/providers](https://github.com/Materials-Consortia/providers)

The repository is organized this way:

- `/src/links/<version>/providers.json` is the current providers.json file formatted according to OPTiMaDe version `<version>` and any later version that uses a format that is backward compatible with this version.

- `/src/links/<version>/info.json` is the proper response to the info endpoint formatted according to OPTiMaDe version `<version>` and any later version that uses a format that is backward compatible with this version.

- `/_redirect` specify http rewrites to map index meta-database URLs `/<version>/info` and `/<version>/links` to the corresponding files under `src/`, as well as `/providers.json`.

- `/<version>` directories contain symlinks `info.html` and `links.html` to the corresponding files under `src/` to somewhat support hosting solutions that do not understand the instructions in `_redirect` but which support "pretty URLs".

- `/providers.json` is a symbolic link continously updated to point at the latest version of the providers.json file under `/src/` to somewhat support hosting solutions that do not understand the instructions in `_redirect`.

To update the list of providers, please file a pull-request against the repository.
This pull-request MUST update ALL the provider.json files `src/links/<version>/providers.json`.
(This way, the current list of providers is updated for implementations across all versions of the OPTiMaDe protocol.)
