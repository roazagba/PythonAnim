<script setup>
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
</script>

<template>
  <NavBar />
  <div class="container-fluid bg-dark text-light py-5 div-background-image">
    <div class="row justify-content-center align-items-center">
      <div class="col-12 text-center">
        <h1 class="display-4 font-weight-bold font-50 family-germania">
          Plateforme d'animation d'algorithmes
        </h1>
      </div>
      <div class="col-lg-3 col-md-4 col-sm-12 mt-4 text-center">
        <router-link
          :to="{ name: 'programmer' }"
          class="btn btn-primary btn-style"
          >Run code</router-link
        >
      </div>
      <div class="col-lg-6 col-md-8 col-sm-12 mt-4 text-center text-md-start">
        <p>
          Une nouvelle façon d'apprendre ! Transformez votre code Python en
          animations dynamiques étape par étape qui donnent vie aux algorithmes.
          Parfait pour les étudiants, les enseignants et les développeurs qui
          cherchent à approfondir leur compréhension de concepts complexes.
        </p>
      </div>
    </div>
  </div>
  <section>
    <div class="container">
      <div class="row">
        <div class="col-sm-5">
          <img
            src="/images/img2.png"
            class="img-fluid"
            alt=""
            srcset="/images/img2.png"
          />
        </div>
        <div class="col-sm-7 pt-5 pt-lg-0">
          <h2 class="fw-bold">Commencer à développer</h2>
          <p style="font-size: 20px; color: #424142">
            Améliorez votre expérience de codage avec notre plateforme
            d'animation d'algorithmes, conçue pour transformer le code Python en
            animations dynamiques étape par étape. Que vous saisissiez votre
            code directement ou que vous téléchargiez un fichier, notre
            plateforme visualise chaque opération algorithmique en temps réel.
          </p>
          <a href="" class="btn btn-primary btn-style">Commencer</a>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-black py-5">
    <div class="container">
      <div>
        <h3 class="fw-bold">
          Comment <label class="text-blue">visualiser</label> l'execution de
          votre code ?
        </h3>
      </div>
      <div
        class="row d-flex d-flex flex-column flex-lg-row justify-content-lg-between mt-5"
      >
        <div
          class="col-lg-4 card rounded mb-lg-5"
          style="background-color: #262125"
        >
          <img
            src="/images/v1.jpg"
            class="card-img-top image-resize img-fluid"
            alt="..."
          />
          <div class="card-body bg-black">
            <h5 class="fw-bold text-primary">Saisissez votre code</h5>
            <p class="fw-light opacity-75" style="color: #f0f1f5 !important">
              Saisissez votre code Python dans l'éditeur fourni, ou téléchargez
              un fichier Python à l'aide de l'option de téléchargement de
              fichier.
            </p>
          </div>
        </div>
        <div
          class="col-lg-4 card rounded mb-lg-5"
          style="background-color: #262125"
        >
          <img
            src="/images/v1.jpg"
            class="card-img-top image-resize img-fluid"
            alt="..."
          />
          <div class="card-body bg-black">
            <h5 class="fw-bold text-primary">Soummettre le code</h5>
            <p class="fw-light opacity-75" style="color: #f0f1f5 !important">
              Cliquez sur le bouton « Soumettre » pour traiter votre code et
              générer l'animation.
            </p>
          </div>
        </div>
        <div
          class="col-lg-4 card rounded mb-lg-5"
          style="background-color: #262125"
        >
          <img
            src="/images/v1.jpg"
            class="card-img-top image-resize img-fluid"
            alt="..."
          />
          <div class="card-body bg-black">
            <h5 class="fw-bold text-primary">Voir l'animation</h5>
            <p class="fw-light opacity-75" style="color: #f0f1f5 !important">
              Regardez l'animation en temps réel, étape par étape, de
              l'exécution de votre algorithme, en utilisant le panneau de
              contrôle pour lire, mettre en pause ou parcourir les étapes.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="bg-footer">
    <div class="container">
      <div>
        <h3 class="text-center fw-bold color-white">
          S'abonner pour être informé des mises à jour.
        </h3>
        <p class="text-center color-white">
          En vous souscrivant avec votre courrier, vous acceptez notre politique
          de confidentialité.
        </p>
      </div>
      <div class="text-center">
        <form class="d-inline-flex">
          <div class="row">
            <div class="col-lg-9 col-sm-6 col-md-9">
              <input
                type="email"
                class="form-control"
                placeholder="Votre email"
              />
            </div>
            <div class="col-lg-3 col-sm-6 col-md-3 mt-2 mt-lg-0">
              <button type="submit" class="btn btn-sm btn-blue btn-style ms-2">
                S'abonner
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>
  <Footer />
</template>
