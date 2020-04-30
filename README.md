<a href="https://www.optimade.org/"><img src="https://avatars0.githubusercontent.com/u/23107754" align="left" width="10%" ></a>

# OPTIMADE Providers Index Meta-Database

The list of OPTIMADE providers keeps track of all reserved database-specific prefixes and the URLs to the index databases of all OPTIMADE database providers that participate in the [OPTIMADE network](https://www.optimade.org/).

The list of providers is published in the form of a statically hosted OPTIMADE Index Meta-Database here:

- [https://providers.optimade.org/](https://providers.optimade.org/)

If you specifically seek the current list of providers for the latest version of the OPTIMADE specification, you can access it at this URL:

- [https://providers.optimade.org/providers.json](https://providers.optimade.org/providers.json)

If you seek the list of providers formatted according to a specific major version of the OPTIMADE specification, you can access it using this URL:

- [https://providers.optimade.org/*\<version\>*/links](https://providers.optimade.org/v1/links)

Where `<version>` designates a major version name of the OPTIMADE specification, e.g., `v1`. 

## Repository organization

The OPTIMADE providers repository is hosted here: [https://github.com/Materials-Consortia/providers](https://github.com/Materials-Consortia/providers)

The repository is organized this way:

- `/src/links/<version>/providers.json` is the current providers.json file formatted according to OPTIMADE version `<version>` and any later version that uses a format that is backward compatible with this version.

- `/src/info/<version>/info.json` is the proper response to the info endpoint formatted according to OPTIMADE version `<version>` and any later version that uses a format that is backward compatible with this version.

- `/_redirect` specify http rewrites to map index meta-database URLs `/<version>/info` and `/<version>/links` to the corresponding files under `src/`, as well as `/providers.json`.

- `/<version>` directories contain symlinks `info.html` and `links.html` to the corresponding files under `src/` to somewhat support hosting solutions that do not understand the instructions in `_redirect` but which support "pretty URLs".

- `/providers.json` is a symbolic link continously updated to point at the latest version of the providers.json file under `/src/` to somewhat support hosting solutions that do not understand the instructions in `_redirect`.

Presently, only the `v1` version of the formats exist.
Hence, to update the list of providers, file a pull-request against the repository to edit `/src/links/v1/providers.json`.
