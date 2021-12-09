

export interface FetchRequest {
    url: string
}

export interface FetchResponse {
    ok: boolean,
    url: string,
    buffer?: ArrayBuffer
    text?: string
}