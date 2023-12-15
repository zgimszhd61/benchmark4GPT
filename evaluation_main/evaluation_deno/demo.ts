const decoder = new TextDecoder('utf-8');
const data = await Deno.readFile('hello.txt');
console.log(decoder.decode(data));
