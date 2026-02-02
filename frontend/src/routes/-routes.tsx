import { createRootRoute, createRoute, Router } from "@tanstack/react-router";
import App from "../App";
import { Index } from "./-main";

export const routerConfigs = [
  {
    path: "/",
    label: "Home",
    component: Index,
  },
];

const rootRoute = createRootRoute({
    component: () => <App />,
})

const childRoutes = routerConfigs.map((cfg) =>
  createRoute({
    getParentRoute: () => rootRoute,
    path: cfg.path,
    component: cfg.component,
  })
);

export const router = new Router({
  routeTree: rootRoute.addChildren(childRoutes),
});
