import log from "lib/Logger"
import type { FetchRequest, FetchResponse } from "lib/FetchMessage"
import WebWorker from 'web-worker:./FetchWorker';

const worker = new WebWorker();

let callbackMap: Map<string,(data:any)=>void> = new Map();

export function request(path: string, callback: (data:any) => void) {
    let proto = window.location.protocol;
    let host = window.location.host
    let url = new URL(path, `${proto}//${host}`);
    log.debug(`url: ${url}`)
    let request: FetchRequest = {
        url: url.toString()
    }
    callbackMap.set(url.toString(),callback);
    worker.postMessage(request);
}

const fetchHandler: EventListener = (e: Event): void => {
    const event = e as MessageEvent;
    const response: FetchResponse = event.data;
    const callback = callbackMap.get(response.url);
    if(callback) {
        callback(response.text);
        log.debug(`invoking callback for ${response.url}`)
    } else {
        log.error(`unrecognized response from: ${response.url}`)
    }
}
worker.addEventListener('message', fetchHandler);