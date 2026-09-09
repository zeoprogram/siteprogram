import { Toaster } from "./components/ui/sonner";
<BrowserRouter>
  <App />
</BrowserRouter>

<Toaster
  position="bottom-right"
  richColors
/>
    import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import "./index.css";
import App from "./App.tsx";
import { queryClient } from "./lib/queryClient";
import { Toaster } from "./components/ui/sonner";

import {
  QueryClientProvider,
} from "@tanstack/react-query";


ReactDOM.createRoot(
  document.getElementById("root")!
).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <App />
      </BrowserRouter>

      <Toaster
        position="bottom-right"
        richColors
      />
    </QueryClientProvider>
  </React.StrictMode>
);
