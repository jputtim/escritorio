// FUNCOES CLIENTES 

var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
  },
  spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
      }
  };
  
  
  django.jQuery(function(){
      
      django.jQuery('.mask-money').mask('000.000.000.000.000,00', {reverse: true});
      django.jQuery('.mask-cpf').mask('000.000.000-00', {reverse: true});
      django.jQuery('.mask-cnpj').mask('00.000.000/0000-00', {reverse: true});
      django.jQuery('.vDateField').mask('00/00/0000');
      django.jQuery('.mask-telefone').mask(SPMaskBehavior, spOptions);
      django.jQuery('.mask-cep').mask('00000-000');
  
      django.jQuery('#sede_form').submit(function(){
          django.jQuery('#sede_form').find(":input[class*='mask-']").unmask();
      });

      // $(document).ready(function() {
        function limpa_formulário_cep() {
            // Limpa valores do formulário de cep.
            django.jQuery("#id_logradouro").val("");
            django.jQuery("#id_bairro").val("");
            django.jQuery("#id_cidade").val("");
            django.jQuery("#id_uf").val("");
            
        }
        
        //Quando o campo cep perde o foco.
        django.jQuery("#id_cep").blur(function() {

            //Nova variável "cep" somente com dígitos.
            var cep = django.jQuery(this).val().replace(/\D/g, '');

            //Verifica se campo cep possui valor informado.
            if (cep != "") {

                //Expressão regular para validar o CEP.
                var validacep = /^[0-9]{8}$/;

                //Valida o formato do CEP.
                if(validacep.test(cep)) {

                    //Preenche os campos com "..." enquanto consulta webservice.
                    django.jQuery("#id_logradouro").val("...");
                    django.jQuery("#id_bairro").val("...");
                    django.jQuery("#id_cidade").val("...");
                    django.jQuery("#id_uf").val("...");
                    
                    //Consulta o webservice viacep.com.br/
                    django.jQuery.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {

                        if (!("erro" in dados)) {
                            //Atualiza os campos com os valores da consulta.
                            django.jQuery("#id_logradouro").val(dados.logradouro);
                            django.jQuery("#id_bairro").val(dados.bairro);
                            django.jQuery("#id_cidade").val(dados.localidade);
                            django.jQuery("#id_uf").val(dados.uf);
                            django.jQuery("#id_numero_residencia").focus();

                        } //end if.
                        else {
                            //CEP pesquisado não foi encontrado.
                            limpa_formulário_cep();
                            alert("CEP não encontrado.");
                        }
                    });
                } //end if.
                else {
                    //cep é inválido.
                    limpa_formulário_cep();
                    alert("Formato de CEP inválido.");
                }
            } //end if.
            else {
                //cep sem valor, limpa formulário.
                limpa_formulário_cep();
            }
        });
    // });
  
  });
  
  