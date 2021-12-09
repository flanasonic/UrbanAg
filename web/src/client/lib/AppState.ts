import type { MenuItemProps } from "components/base/MenuItemProps";
import type { SvelteComponent } from "svelte";
import { writable } from "svelte/store";

class OpenCloseable {
    private _isOpenStore = writable<boolean>(false);
    private _isOpen: boolean = false;

    public constructor() {
        this._isOpenStore.subscribe( value => {
            this._isOpen = value;
        });
    }

    readonly isOpen = ():boolean => {
        return this._isOpen
    }

    readonly open = ():void => {
        if (!this._isOpen) {
            this._isOpenStore.set(true);
        }
    }

    readonly close = ():void => {
        if (this._isOpen) {
            this._isOpenStore.set(false);
        }
    }

    readonly toggle = ():void => {
        if(this._isOpen) {
            this.close();
        } else {
            this.open();
        }
    }
    
    public subscribe( callback: (value: boolean) => void ): () => void {
        return this._isOpenStore.subscribe(callback);
    }

}

class Menu {
    public visibility = new OpenCloseable()
    public items = writable<MenuItemProps>(undefined);    
}

class GlobalState {
    sideMenu = new Menu();
    remoteFiles = writable<Array<string>>(new Array<string>());
}

const globalState = new GlobalState();
export default globalState;