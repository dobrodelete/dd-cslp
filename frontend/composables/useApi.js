export function useApi(resource) {
  const baseUrl = 'http://localhost:8000/api/v1';

  async function callApi(endpoint, options = {}) {
    const { method = 'GET', body } = options;
    const headers = { 'Content-Type': 'application/json' };
    const config = {
      method,
      headers,
      body: body ? JSON.stringify(body) : undefined,
    };

    if (!body) delete config.body;

    const response = await fetch(`${baseUrl}/${resource}/${endpoint}`, config);
    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`);
    }
    return await response.json();
  }

  const create = (data) => callApi('', { method: 'POST', body: data });
  const get = (id) => callApi(`${id}`);
  const list = (options = {}) => callApi(`?${new URLSearchParams(options).toString()}`);
  const update = (id, data) => callApi(`${id}`, { method: 'PUT', body: data });
  const remove = (id) => callApi(`${id}`, { method: 'DELETE' });

  return { create, get, list, update, remove };
}
