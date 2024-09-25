<script setup>
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import hljs from "highlight.js";
import CodeEditor from "simple-code-editor";
import axios from "axios";
import { ref, computed } from "vue";

const form = ref({
  code: "",
  file: "",
});

const steps = ref([]);
const exec = ref(false),
  is_error = ref(false),
  errors = ref("");
const current_step_index = ref(0);
const is_paused = ref(true);
const interval = ref(null);
const display_output = ref("");

const formatCode = (code) => {
  return code
    .replace(/[\u00A0]/g, " ")
    .replace(/\\/g, "\\\\")
    .replace(/\n/g, "\n")
    .replace(/\t/g, "\\t")
    .replace(/"/g, '"');
};

const file = ref(""),
  filename = ref(""),
  file_uploaded = ref(false),
  file_content = ref("");
const onLoadPythonFile = (e) => {
  file.value = e.target.files[0];

  if (file) {
    if (file.value.name.endsWith(".py")) {
      file_uploaded.value = true;
      filename.value = file.value.name;
      let reader = new FileReader();
      reader.onload = (event) => {
        file_content.value = event.target.result;
      };

      reader.readAsText(file.value);
    }
  }
};

const runCode = async () => {
  try {
    (exec.value = false), (is_error.value = false);
    //let formatted_code = JSON.stringify(form.value.code)
    let formatted_code = "";
    if (file_uploaded.value) {
      formatted_code = formatCode(file_content.value);
    } else {
      formatted_code = formatCode(form.value.code);
    }

    const response = await axios.post(
      `${import.meta.env.VITE_APP_URL}/execute`,
      {
        code: formatted_code,
      }
    );

    let reponse = response.data;
    if (reponse.output != "") {
      let output = reponse.output.split("\n");
      output.pop();

      let output_final = output.map((element) => {
        return element.replace(/\\n/g, "");
      });

      exec.value = true;
      file_uploaded.value = false;
      steps.value = output_final;
      current_step_index.value = 0;
      display_output.value = "";
      is_paused.value = true;
    }
  } catch (error) {
    is_error.value = true;
    errors.value = error.response.data.error;
  }
};

const displayed_lines = computed(() => {
  return steps.value.slice(0, current_step_index.value + 1);
});

const play = () => {
  is_paused.value = false;
  interval.value = setInterval(() => {
    nextStep();
  }, 1000);
};

const pause = () => {
  is_paused.value = true;
  clearInterval(interval.value);
};

const nextStep = () => {
  if (current_step_index.value < steps.value.length - 1) {
    const step = steps.value[current_step_index.value];
    display_output.value += step + "\n";
    current_step_index.value++;
  } else {
    pause();
  }
};

const prevStep = () => {
  if (current_step_index.value > 0) {
    current_step_index.value--;
    const step = steps.value[current_step_index.value];

    display_output.value = display_output.value
      .split("\n")
      .slice(0, -1)
      .join("\n");
  }
};

const reset = () => {
  current_step_index.value = -1;
  display_output.value = "";
  pause();
};

const downloadSteps = () => {
  const blob = new Blob([JSON.stringify(steps.value, null, 2)], {
    type: "application/json",
  });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.setAttribute("download", "steps.json");
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};
</script>

<template>
  <NavBar />
  <div class="container-fluid bg-dark text-light py-5 div-background-image">
    <div class="row justify-content-center align-items-center">
      <div class="col-12 text-center">
        <h1 class="display-4 font-weight-bold font-50 family-germania">
          Coder For Life
        </h1>
      </div>
    </div>
  </div>

  <section>
    <div class="container-fluid">
      <div>
        <h3 class="text-center fw-bold">
          Soumettez votre code Python pour en visualiser l'exécution.
        </h3>
      </div>
      <div class="row mt-5">
        <div class="col-sm-6">
          <form
            method="post"
            @submit.prevent="runCode"
            enctype="multipart/form-data"
          >
            <div class="row d-flex justify-content-between">
              <div class="col-9 fw-bold">
                Saisissez le code python ou importer le fichier python
              </div>
              <div class="col-3">
                <input
                  type="file"
                  id="file-python"
                  class="d-none"
                  accept=".py"
                  v-on:change="onLoadPythonFile"
                />
                <label
                  type="button"
                  for="file-python"
                  class="btn btn-sm btn-blue"
                >
                  Importer <i class="bi bi-upload"></i>
                </label>
                <div v-if="file_uploaded">
                  Fichier <b>{{ filename }}</b> téléversé avec succès.
                </div>
              </div>
            </div>
            <code-editor
              theme="atom-one-dark"
              :tab-spaces="4"
              :line-nums="true"
              style="margin: 5px 0px 5px"
              v-model="form.code"
              width="100%"
              height="500px"
              :languages="[['python', 'Python']]"
            ></code-editor>
            <button type="submit" class="btn btn-sm btn-success me-3">
              Exécuter <i class="bi bi-play-fill"></i>
            </button>
          </form>
        </div>
        <div class="col-sm-6" style="padding-top: 3rem" v-if="exec">
          <div class="display-steps">
            <transition-group name="list" tag="div">
              <div
                v-for="(line, index) in displayed_lines"
                :key="index"
                class="line"
              >
                {{ line }}
              </div>
            </transition-group>
          </div>
          <div class="mt-2">
            <button @click="prevStep" class="btn btn-secondary me-3">
              <i class="bi bi-arrow-left-short"></i>
            </button>
            <button
              @click="play"
              class="btn btn-secondary me-3"
              v-if="is_paused"
            >
              <i class="bi bi-play-fill"></i>
            </button>
            <button @click="pause" class="btn btn-secondary me-3" v-else>
              <i class="bi bi-pause-btn-fill"></i>
            </button>
            <button @click="nextStep" class="btn btn-secondary me-3">
              <i class="bi bi-arrow-right-short"></i>
            </button>
            <button @click="reset" class="btn btn-secondary me-3">
              <i class="bi bi-arrow-clockwise"></i>
            </button>
            <button @click="downloadSteps" class="btn btn-secondary me-3">
              <i class="bi bi-download"></i>
            </button>
          </div>
        </div>
        <div class="col-5" style="padding-top: 3rem" v-if="is_error">
          <div class="display-steps">{{ errors }}</div>
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
<style scoped>
.display-steps {
  background-color: #282c34;
  color: #fff;
  height: 32rem;
  border-radius: 10px;
  padding: 20px;
  overflow: scroll;
  margin-top: -13px;
}

.line {
  padding: 5px;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>
