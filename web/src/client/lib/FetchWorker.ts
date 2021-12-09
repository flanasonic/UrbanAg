
import log from "./Logger"
import type { FetchRequest, FetchResponse } from "./FetchMessage"
declare var self: DedicatedWorkerGlobalScope;

const handler: EventListener = (e: Event) : void => {
    const event = e as MessageEvent;
    const request: FetchRequest = event.data;
    log.trace(`Fetching ${request.url}`)
    fetch(request.url).then(sendResponse);
}
self.addEventListener('message', handler)

async function sendResponse(response: Response): Promise<void> {
    log.debug("sending response...")
    let text: string = await response.text();
    log.debug(`got text ${text}`)
    let result :FetchResponse = {
        ok: true,
        url: response.url,
        text
    }
    self.postMessage(result);
}  