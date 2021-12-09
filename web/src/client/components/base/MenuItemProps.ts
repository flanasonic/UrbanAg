
export class MenuAction {
    text: string = "[undefined]"
    action: () => void = ()=>{};
}


export class MenuItemProps {
    public actions: Array<MenuAction> = new Array()
}