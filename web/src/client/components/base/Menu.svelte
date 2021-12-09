<script lang="ts" context="module">
    import { MenuAction, MenuItemProps } from "./MenuItemProps";
    import state from "lib/AppState"
    const defaultItems = new MenuItemProps()
</script>
<script lang="ts">
    import VirtualList from "@sveltejs/svelte-virtual-list"
    export let title: string = "[menu]";
    export let menuProps = defaultItems
    type item = MenuAction

    function menuSelect(action: ()=>void) {
        state.sideMenu.visibility.close();
        action();
    }

</script>

<h1>{title}</h1>
<VirtualList items={menuProps.actions} let:item>
<div class="menuitem" on:click={() => {menuSelect(item.action)}}>{item.text}</div>
</VirtualList>

<style>
.menuitem {
    padding: 5px 10px 10px 5px;
    border-bottom: 1px solid black;
}
</style>