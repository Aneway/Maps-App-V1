<template>
  <ion-app>
    <ion-header>
      <ion-grid>
        <ion-row>
          <ion-col>
            <div id="slogan"></div>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-header>

    <ion-content scrolly="false" :fullscreen="true">
      <ion-grid>
        <ion-row id="inputs">
          <ion-col id="colInput">
            <h1>Register</h1>
            <ion-item>
              <ion-label position="stacked">EDV</ion-label>
              <ion-input v-model="edv" disabled></ion-input>
            </ion-item>
            <ion-item>
              <ion-label position="stacked">Name</ion-label>
              <ion-input v-model="name" disabled></ion-input>
            </ion-item>
            <ion-item>
              <ion-label position="floating">Password</ion-label>
              <ion-input v-model="password" type="password"></ion-input>
            </ion-item>
            <ion-item>
              <ion-label position="floating">Confirm Password</ion-label>
              <ion-input v-model="confirmPassword" type="password"></ion-input>
            </ion-item>
            <!-- <ion-datetime presentation="date"></ion-datetime> -->
            <div id="button">
              <ion-button @click="makeRegister" id="buttonConfirm"
                >Enter</ion-button
              >
            </div>
            <router-link to="/">Cancel</router-link>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>

    <ion-footer>
      <ion-grid>
        <ion-row>
          <ion-col id="colunaFaixa">
            <div id="faixa"></div>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-footer>
  </ion-app>
</template>

<script>
import { userData } from "../store/userInformations";
import {
  IonApp,
  IonInput,
  IonCol,
  IonRow,
  IonGrid,
  IonHeader,
  IonLabel,
  IonItem,
  IonButton,
  IonContent,
  IonFooter,
  alertController,
} from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";
// import { IonDatetime } from '@ionic/vue';

export default defineComponent({
  name: "RegisterScreen",
  components: {
    IonApp,
    IonInput,
    IonCol,
    IonRow,
    IonGrid,
    IonHeader,
    IonLabel,
    IonItem,
    IonButton,
    IonContent,
    IonFooter,
  },
  data() {
    return {
      edv: "",
      name: "",
      password: "",
      confirmPassword: "",
    };
  },
  mounted() {
    if (userData().edv == null) {
      this.$router.push("/");
    }
    this.setFields();
  },
  methods: {
    async NullPassword() {
      const alert = await alertController.create({
        header: "Password field must be filled ",
        subHeader: "Fill the fields and try again",
        buttons: ["Ok"],
      });

      await alert.present();
    },
    async differentPassword() {
      const alert = await alertController.create({
        header: "Passwords are different ",
        subHeader: "check the field and try again",
        buttons: ["Ok"],
      });

      await alert.present();
    },
    makeRegister() {
      if (this.password != "") {
        if (this.password == this.confirmPassword) {
          this.registerNow();
        } else {
          this.differentPassword();
        }
      } else {
        this.NullPassword();
      }
    },
    setFields() {
      const information = userData();
      this.edv = information.edv;
      this.name = information.name;
    },
    registerNow() {
      axios
        .post("http://127.0.0.1:5000/register", {
          EDV: userData().edv,
          Name: userData().name,
          Email: userData().email,
          Phone: userData().telefone,
        })
    },
  },
});
</script>

<style scoped>
* {
  margin: 0px;
  padding: 0px;
}
ion-header {
  height: 10%;
}
h1 {
  align-items: center;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}
#container {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
}

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;
  color: #8c8c8c;
  margin: 0;
}

#container a {
  text-decoration: none;
}
#ion-text {
  text-align: center;
}
#slogan {
  background-image: url("../../public/assets/logotype.svg");
  background-size: contain;
  height: 70px;
  background-repeat: no-repeat;
}
#button {
  align-items: center;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}
a {
  padding: 20px;
  align-items: center;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}
#buttonConfirm {
  --background: #0a6f9d;
  width: 30%;
  margin-top: 10%;
  --border-radius: 0px;
}
#colunaFaixa {
  height: 10%;
}
#inputs {
  margin-top: 60px;
}
#colInput {
  width: 40%;
}
#faixa {
  height: 10px;
  background-image: url("../../public/assets/supergrafic.svg");
  background-repeat: no-repeat;
  background-size: cover;
}
</style>