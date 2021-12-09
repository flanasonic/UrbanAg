

export namespace log {
function logger(level:string, message: string): void {
    let now = new Date().toLocaleDateString();
    console.log(`${now} [${level}]: ${message} `);
}
    export function trace(message: string): void {
        logger("trace", message);
    }

    export function debug(message: string): void {
        logger("debug", message);
    }

    export function error(message: string): void {
        logger("ERROR", message);
    }
}

export default log;