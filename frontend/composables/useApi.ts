export const useApi = () => {
  const config = useRuntimeConfig()

  const get = <T>(endpoint: string) =>
    useFetch<T>(`${config.public.apiBase}${endpoint}`)

  return { get }
}