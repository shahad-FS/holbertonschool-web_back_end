function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({
      status: 200,
      body: 'success',
    }))
    .catch(() => new Error())
    .finally(console.warn.bind(console, 'Got a response from the API'));
}

export default handleResponseFromAPI;
