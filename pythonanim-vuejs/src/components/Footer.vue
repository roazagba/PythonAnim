<template>
  <footer class="pb-5 pt-5 bg-footer">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-sm-6">
          <label class="fw-bold color-white" style="font-size: 25px"
            >PythonAnim</label
          >
        </div>
        <div
          class="col-sm-6 d-flex flex-column flex-lg-row justify-content-lg-between mt-3 mt-lg-0"
        >
          <router-link
            :to="{ name: 'home' }"
            class="text-black text-decoration-none mb-2 mb-lg-0 color-white"
            >Home</router-link
          >

          <router-link
            :to="{ name: 'programmer' }"
            class="text-black text-decoration-none mb-2 mb-lg-0 color-white"
            >Run code</router-link
          >

          <router-link
            :to="{ name: 'contact' }"
            class="text-black text-decoration-none mb-2 mb-lg-0 color-white"
            >Contact</router-link
          >

          <a
            href="#"
            class="text-black text-decoration-none mb-2 mb-lg-0 color-white"
          >
            <i class="bi bi-envelope-fill"></i> us@us.com
          </a>

          <a href="#" class="text-black text-decoration-none color-white">
            <i class="bi bi-telephone-fill"></i> 00 00 00 00
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>
