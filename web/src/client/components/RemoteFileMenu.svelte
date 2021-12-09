<script lang="ts">
    import { request } from "lib/DataFetcher";
    import state from "lib/AppState";
    import { MenuItemProps, MenuAction } from "components/base/MenuItemProps";
    import Menu from "components/base/Menu.svelte";

    export let callback = (contents: string) => {};
    export let menuitems = new MenuItemProps();

    state.remoteFiles.subscribe((updatedFiles) => {
        let newItems = new MenuItemProps();
        for (let file of updatedFiles) {
            let action = new MenuAction();
            action.text = file;
            action.action = () => {
                request(file, callback);
            };
            newItems.actions.push(action);
        }
        menuitems = newItems;
    });
</script>

<Menu title="Files" menuProps={menuitems} />
