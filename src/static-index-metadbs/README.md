# Static Index Meta-Databases

## Goal

This folder hosts static versions of Index Meta-Databases for those providers that only have one main sub-database (or very few sub-databases) and do not wish to maintain an Index Meta-Database themselves (Index Meta-Databases are described in the OPTIMADE specifications).

Note: while providing an (empty) Index Meta-Database is not required by the OPTIMADE API specifications, it is instead required in order to be listed in this List of Providers (http://providers.optimade.org).

## When should I use a static index meta-database hosted in this repository

If you add a new provider and do not wish to host an Index Meta-Database yourself, feel free to add an Index Meta-Database here.

However, if your Index Meta-Database is rapidly changing (e.g. because the list of sub-databases changes often), please host it yourself to avoid multiple commits and pull requests to this repository at every change.
Rare changes are instead of course welcome, e.g., if you have to change your DNS name or the description, or if you need just to add one static new sub-database, like a test database.

Note that "changes" here refer solely to changes to the *list of sub-databases*; the content of each sub-database can change at any time without the need to modify the Index Meta-Database.

## Instructions on how to add a new static Index Meta-Database
1. Go in the folder `src/static-index-metadbs`, copy one of the existing folders (e.g. `cod`) to a new folder, where the folder name should be the identifier of your provider (we will use `exmpl` here and in the following).
   In particular, this will contain a `v1` subfolder, with two files inside it: `info.json` and `links.json`.

2. Adapt the content of the `links.json` file. In particular, provide a new `link` dictionary entry for each sub-database that you want to refer to. 
   In the special case in which you have a single "main" sub-database, just change the existing values as follows:
    
   - change the `id` to your provider identifier: `"cod" -> "exmpl"`
   - change the attributes `name`, `description` and `homepage` to contain the correct content. Please reuse the *same* content as the one you specified in the main `providers.json` file.
   - point the `base_url` to the base URL of your OPTIMADE implementation.

3. Adapt the content of the `info.json` file. In particular, you should change two fields:

   - change the URL of the `available_api_versions` by replacing `cod` with your identifier: `http://providers.optimade.org/index-metadbs/exmpl/v1/`
   - change the `id` inside `data->relationships->default->data->id` to the correct ID from the list of links in the `links.json` file.
     As explained in the OPTIMADE specifications, this should be the ID of the database that should be considered as the "default" sub-database by clients. 
     
     If you only have one sub-database and you followed the instructions above, you should use here your provider identifier.
     If you do not wish to have a default database, remove completely the `relationships` attribute.

4. Go to the top-level folder of this repository, and then to the subfolder `index-metadbs`. Create a subfolder `exmpl` (replace with your provider identifier), and a subfolder `exmpl/v1`.

5. Inside the `exmpl/v1` folder, create two symbolic links pointing to the `info.json` and `links.json` files you created earlier, **but with a `.html` extension**.
   You can simply use the following two commands (replace as usual `exmpl` with your provider ID):

   ```bash
   ln -s ../../../src/static-index-metadbs/exmpl/v1/info.json info.html
   ln -s ../../../src/static-index-metadbs/exmpl/v1/links.json links.html
   ```

6. In the top-level `providers.json` file, point the `base_url` of your provider to `http://providers.optimade.org/index-metadbs/exmpl/`.

7. Create a pull request, and check that all automated continuous-integration tests pass.
