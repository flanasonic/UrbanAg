<script lang="ts">
    import { onMount } from "svelte";
    import { tweened } from "svelte/motion";
    import Ripple from "./Ripple.svelte";
    import { writable } from "svelte/store";

    export let rippleBlur: number = 2;
    export let speed: number = 500;
    export let color: string = "#fff";
    export let fontSize: string = "1rem";
    export let bgColor: string = "93, 120, 255";
    export let bgHover: string = bgColor;
    export let bgActive: string = bgColor;
    export let rippleColor: string = "#264169";
    export let round: string = "0.5rem";
    export let height: number = 60;
    export let width: number = 250;
    export let sizeIn: number = 20;
    export let opacityIn: number = 0.2;
    export let shadow: string = "none";
    export let shadowHover: string = "none";
    export let shadowActive: string = "none";
    export let onClick: Function = () => null;

    interface ShadowMap {
        [key: string]: string;
    }

    let shadows: ShadowMap = {
        none: "none",
        1: "0 0 0 1px rgba(0, 0, 0, 0.05)",
        2: "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
        3: "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)",
        4: "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        5: "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        6: "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
        7: "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
    };

    let mouseX: number = 0;
    let mouseY: number = 0;
    let rect: DOMRect;
    let rippleBtn: HTMLButtonElement;
    let w: number;
    let h: number;
    let x: number;
    let y: number;
    let offsetX: number;
    let offsetY: number;
    let deltaX: number;
    let deltaY: number;
    let locationY: number;
    let locationX: number;
    let scale_ratio: number;
    let timer: number;

    interface Ripple {
        x: number;
        y: number;
        size: number;
    }

    function handleRipple() {
        const ripples = writable<Ripple[]>([]);

        return {
            subscribe: ripples.subscribe,

            add: (item: Ripple) => {
                ripples.update((items) => {
                    return [...items, item];
                });
            },
            clear: () => {
                ripples.update((_) => {
                    return [];
                });
            },
        };
    }

    export const ripples = handleRipple();

    let coords = { x: 50, y: 50 };

    $: (offsetX = Math.abs(w / 2 - coords.x)),
        (offsetY = Math.abs(h / 2 - coords.y)),
        (deltaX = w / 2 + offsetX),
        (deltaY = h / 2 + offsetY),
        (scale_ratio = Math.sqrt(Math.pow(deltaX, 2.2) + Math.pow(deltaY, 2.2)));

    const debounce = () => {
        clearTimeout(timer);
        timer = setTimeout(() => {
            ripples.clear();
        }, speed + speed * 2);
    };

    let touch: boolean;

    type ClickEvent = MouseEvent | Touch;

    function handleClick(e: ClickEvent, type: string) {
        if (type == "touch") {
            touch = true;
            ripples.add({
                x: e.pageX - locationX,
                y: e.pageY - locationY,
                size: scale_ratio,
            });
        } else {
            if (!touch) {
                ripples.add({
                    x: e.clientX - locationX,
                    y: e.clientY - locationY,
                    size: scale_ratio,
                });
            }
            touch = false;
        }
        onClick();
        debounce();
    }

    onMount(() => {
        w = rippleBtn.offsetWidth;
        h = rippleBtn.offsetHeight;
        rect = rippleBtn.getBoundingClientRect();
        locationY = rect.y;
        locationX = rect.x;
    });
</script>

<button
    on:click
    style="
    --color: {color}; 
    --font-size: {fontSize};
    --bg-color: {bgColor}; 
    --bg-hover: {bgHover};
    --bg-active: {bgActive};
    --radius: {round};
    --ripple: {rippleColor};
    --height: {height}px;
    --width: {width}px; 
    --shadow: {shadows[shadow]};
    --shadow-h: {shadows[shadowHover]};
    --shadow-a: {shadows[shadowActive]}"
    bind:this={rippleBtn}
    on:touchstart={(e) => handleClick(e.touches[0], "touch")}
    on:mousedown={(e) => handleClick(e, "click")}
>
    <span>
        <slot />
    </span>
    <svg>
        {#each $ripples as ripple, index}
            <Ripple x={ripple.x} y={ripple.y} size={ripple.size} {speed} {sizeIn} {opacityIn} {rippleBlur} />
        {/each}
    </svg>
</button>

<style>
    button {
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        border: none;
        font-weight: 500;
        color: var(--color);
        font-size: var(--font-size);
        height: var(--height);
        width: var(--width);
        max-width: 100%;
        margin: 0;
        padding: 0;
        position: absolute;
        border-radius: var(--radius);
        cursor: pointer;
        -webkit-transition: 200ms all ease-out;
        transition: 200ms all ease-out;
        background-color: rgba(var(--bg-color), 1);
        overflow: hidden;
        font-family: Roboto, sans-serif;
        box-shadow: var(--shadow);
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        -webkit-tap-highlight-color: transparent;
    }

    button:hover,
    button:focus {
        outline: none;
        background-color: rgba(var(--bg-hover), 0.8);
        box-shadow: var(--shadow-h);
    }
    button:active {
        outline: none;
        background-color: rgba(var(--bg-active), 0.7);
        box-shadow: var(--shadow-a);
    }
    span {
        position: relative;
        height: 50%;
        width: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0;
        left: 10px;
        padding: 0;
        z-index: 1;
    }
    svg {
        height: 100%;
        width: 100%;
        pointer-events: none;
        position: absolute;
        top: 0;
        left: 0;
        z-index: 0;
    }
</style>
