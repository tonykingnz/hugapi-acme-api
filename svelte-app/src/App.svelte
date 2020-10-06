<script>
	export let name;
    import AutoComplete from "simple-svelte-autocomplete";

    const books = ["Lord of the Rings", "Hobbit", "Moby-Dick", "1984", "Hamlet", "The Adventures of Sherlock Homes"];
    let selectedBooks;

</script>

<main>
	<h1>Search for books names below {name}!</h1>
	<AutoComplete items={books} bind:selectedBooks={selectedBooks} />
    <p>Visit the <a href="https://github.com/pstanoev/simple-svelte-autocomplete">Simple Svelte Autocomplete</a> to learn how to build typeahead in Svelte apps.</p>
    <p>Made by <a href="https://github.com/tonyKingNZ">@tonyKingNZ</a> to {name}</p> 
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
