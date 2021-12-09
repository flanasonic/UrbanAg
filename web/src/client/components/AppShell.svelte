<script lang="ts">
    import { request } from "lib/DataFetcher";
    import state from "lib/AppState";
    import Button from "components/base/Button.svelte";
    import Hamburger from "./icons/Hamburger.svelte";
    import Drawer from "components/Drawer.svelte";
	import RemoteFileMenu from "components/RemoteFileMenu.svelte"

    import { onMount } from "svelte";

    export let name: string;

    let data = "";

    function dataHandler(newData: any) {
        data = newData;
    }

    onMount(async () => {
        request("/api/files", (data) => { state.remoteFiles.set(JSON.parse(data)); } );
    });

    const buttonProps = {
        height: 40,
        width: 40,
        round: "2rem",
        rippleColor: "#999",
        opacityIn: 0.5,
        sizeIn: 10,
        color: "#333",
        bgColor: "255, 255, 255",
        bgHover: "245, 245, 245",
        bgActive: "200, 200, 200",
        rippleBlur: 9,
        onClick: state.sideMenu.visibility.toggle,
    };
</script>

<main>
    <Button {...buttonProps}>
        <Hamburger />
    </Button>
    <Drawer><RemoteFileMenu callback={dataHandler} /> </Drawer>
    <pre>{data}</pre>
</main>

<style>
    main {
        padding: 0;
        margin: 0 auto;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>
