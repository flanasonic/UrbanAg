<script lang="ts">
    import state from "lib/AppState";
    export let open: boolean = false;
    state.sideMenu.visibility.subscribe((value) => { open = value; })
</script>

<div class="drawer-base drawer" class:open>
<slot></slot>
</div>

<style>
    .drawer-base {
        top: 40px;
    }

    .drawer {
        position: absolute;
        height: 70vh;
        left: -100%;
        transition: left 0.3s ease-in-out;
        border: 1px solid black;
        background-color: white;
    }

    .open {
        left: 0%;
    }
</style>
