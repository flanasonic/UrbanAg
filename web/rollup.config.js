import alias from '@rollup/plugin-alias'
import svelte from 'rollup-plugin-svelte';
import commonjs from '@rollup/plugin-commonjs';
import resolve from '@rollup/plugin-node-resolve';
import typescript from 'rollup-plugin-typescript2';
import workerLoader from 'rollup-plugin-web-worker-loader';
import sveltePreprocess from 'svelte-preprocess';
import livereload from 'rollup-plugin-livereload';
import { terser } from 'rollup-plugin-terser';
import css from 'rollup-plugin-css-only';
import copy from 'rollup-plugin-copy';
import { writeFileSync } from 'fs';

const production = !process.env.ROLLUP_WATCH;
const extensions = [
    '.js', '.jsx', '.ts', '.tsx',
];

function serve() {
	let server;

	function toExit() {
		if (server) server.kill(0);
	}

	return {
		writeBundle() {
			if (server) return;
			server = require('child_process').spawn('npm', ['run', 'start', '--', '--dev'], {
				stdio: ['ignore', 'inherit', 'inherit'],
				shell: true
			});

			process.on('SIGTERM', toExit);
			process.on('exit', toExit);
		}
	};
}

export default {
	input: 'src/client/main.ts',
	output: {
		sourcemap: true,
		format: 'iife',
		name: 'app',
		file: 'dist/js/bundle.js'
	},
	plugins: [
		svelte({
			preprocess: sveltePreprocess({ sourceMap: !production }),
			compilerOptions: { dev: !production }
		}),
		css({
			output: (styles, styleNodes) => { writeFileSync('dist/css/bundle.css', styles); }
		}),
		resolve({
			extensions,
			browser: true,
			dedupe: ['svelte']
		}),
		commonjs(),
		workerLoader({extensions}),
		typescript(),
		alias({
			entries: [
				{ find: /^lib(\/|$)/, replacement: `${__dirname}/src/client/lib/` },
				{ find: /^components(\/|$)/, replacement: `${__dirname}/src/client/components/` }
			]
		}),

		copy({
			targets: [
				{ src: "src/client/static/*", dest: "dist" }
			]
		}),

		// Calls`npm run start` once
		!production && serve(),
		!production && livereload('dist'),
		production && terser()
	],
	watch: {
		clearScreen: false
	}
};
