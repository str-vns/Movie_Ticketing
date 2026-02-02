import { StrictMode } from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/react-router-devtools";
import { router } from "@_/routes/-routes"
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import './index.css'; 
import './App.css';

declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}

const queryClient = new QueryClient()

const rootElement = document.getElementById("root")!;
if (!rootElement.innerHTML) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <StrictMode>
       <QueryClientProvider client={queryClient}>
      <RouterProvider router={router} />
      {import.meta.env.VITE_BUILD === "DEV" && <TanStackRouterDevtools initialIsOpen={false} router={router} position="bottom-right" /> }
    </QueryClientProvider>
    </StrictMode>
  );
}
