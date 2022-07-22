import {defineStore} from 'pinia'

export const userData = defineStore('userData', {
    state:()=>{
        return{
            edv:null,
            name:null,
            email:null,
            telefone:null,
        }
    },
    actions: {
        inputData(edv,name,email,telefone){
            this.edv = edv,
            this.name = name,
            this.email = email,
            this.telefone = telefone
        }
    }
})