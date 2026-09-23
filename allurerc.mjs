import { defineConfig } from "allure";

const browsers = ["chromium", "firefox", "webkit"];

export default defineConfig({
  output: "./allure-report",
  environments: {
    chromium: {
      name: "Chromium",
      matcher: ({ labels }) =>
        labels.some((l) => l.name === "browser" && l.value === "chromium"),
    },
    firefox: {
      name: "Firefox",
      matcher: ({ labels }) =>
        labels.some((l) => l.name === "browser" && l.value === "firefox"),
    },
    webkit: {
      name: "WebKit",
      matcher: ({ labels }) =>
        labels.some((l) => l.name === "browser" && l.value === "webkit"),
    },
  },
});