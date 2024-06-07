
interface FetchOptions extends RequestInit {
    url: string;
  }
  
  const fetchApi = async <T>({ url, ...options }: FetchOptions): Promise<T> => {
    const accessToken = localStorage.getItem('access_token');
  
    const headers = new Headers(options.headers || {});
    if (accessToken) {
      headers.append('Authorization', `Bearer ${accessToken}`);
    }
  
    const response = await fetch(url, {
      ...options,
      headers
    });
  
    if (!response.ok) {
      throw new Error('Сетевая ошибка при выполнении запроса');
    }
  
    const data = await response.json() as T;
    return data;
  }
  
  export default fetchApi;
  