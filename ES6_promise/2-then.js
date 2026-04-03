function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({
      status: 200,
      body: 'success',
    }))
    .catch(() => {
      return new Error();
    })
    .then((result) => {
      console.warn('Got a response from the API');
      return result;
    });
}

export default handleResponseFromAPI;
