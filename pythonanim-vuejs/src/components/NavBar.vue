<script setup>
import { useRoute } from "vue-router";
const route = useRoute();

const isActiveRoute = (name) => {
  return route.name === name;
};
</script>
<template>
  <nav class="navbar navbar-expand-lg bg-light luxe-navbar p-4">
    <div
      class="container-fluid"
      style="padding-left: 10vw !important; padding-right: 10vw !important"
    >
      <router-link class="navbar-brand text-white" :to="{ name: 'home' }"
        >PythonAnim</router-link
      >
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div
        class="collapse navbar-collapse d-lg-flex justify-content-lg-end"
        id="navbarNavAltMarkup"
      >
        <div class="navbar-nav">
          <router-link
            aria-current="page"
            :class="{ 'text-primary': isActiveRoute('home') }"
            class="nav-link text-white ms-5"
            :to="{ name: 'home' }"
            >Home</router-link
          >
          <router-link
            class="nav-link text-white ms-5"
            :class="{ 'text-primary': isActiveRoute('programmer') }"
            :to="{ name: 'programmer' }"
            >Run Code</router-link
          >
          <router-link
            class="nav-link text-white ms-5"
            :class="{ 'text-primary': isActiveRoute('contact') }"
            :to="{ name: 'contact' }"
            >Contact</router-link
          >
        </div>
      </div>
    </div>
  </nav>
</template>
