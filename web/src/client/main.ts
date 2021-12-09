import App from './components/AppShell.svelte';

const app = new App({
	target: document.body,
	props: {
		name: 'Julie'
	}
});

export default app;