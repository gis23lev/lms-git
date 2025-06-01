import React, { useState } from 'react';
import Icon from 'react-native-vector-icons/FontAwesome';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  Alert,
  KeyboardAvoidingView,
  Platform,
  Image,
} from 'react-native';

export default function LoginScreen({ navigation }) {
  const [nombre, setNombre] = useState('');
  const [ci, setCi] = useState('');

  const handleLogin = async () => {
    if (!nombre || !ci) {
      Alert.alert('Campos requeridos', 'Por favor ingresa tu usuario y contraseña.');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:8000/api/estudiante/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nombre, password: ci }),
      });

      const data = await response.json();

      if (data.success) {
        Alert.alert('Bienvenido/a', `Hola, ${data.estudiante.nombre}`);

        navigation.navigate('DashboardEstudiante');
      } else {
        Alert.alert('Error', data.message || 'Credenciales incorrectas');
      }
    } catch (error) {
      Alert.alert('Error de conexión', 'No se pudo conectar con el servidor.');
    }
  };

  return (
    <KeyboardAvoidingView
      style={styles.container}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    >
      <View style={styles.logoContainer}>
        <Image source={require('../assets/logo.png')} style={styles.logo} />
      </View>

      {/* <Text style={styles.title}>Inicie Sesión</Text> */}

      <View style={styles.card}>
        {/* <Text style={styles.subtitle}>Ingrese sus datos</Text> */}
        <View style={styles.labelContainer}>
          <Icon name="user" size={18} color="#2D3748" style={styles.icon} />
          <Text style={styles.labelText}> Usuario:</Text>
        </View>
        <TextInput
          value={nombre}
          onChangeText={setNombre}
          placeholder="Usuario "
          placeholderTextColor="#999"
          style={styles.input}
        />

        <View style={styles.labelContainer}>
          <Icon name="lock" size={18} color="#2D3748" style={styles.icon} />
          <Text style={styles.labelText}> Contraseña:</Text>
        </View>
        <TextInput
          value={ci}
          onChangeText={setCi}
          placeholder="Contraseña"
          placeholderTextColor="#999"
          keyboardType="numeric"
          secureTextEntry
          style={styles.input}
        />

        <TouchableOpacity style={styles.button} onPress={handleLogin}>
          <Text style={styles.buttonText}>Iniciar Sesión</Text>
        </TouchableOpacity>
      </View>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#E6F0FA',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  logoContainer: {
    position: 'center',
    top: 15,
    marginBottom:10,
  },
  logo: {
    width: 170,
    height: 170,
    resizeMode: 'contain',
  },
  // title: {
  //   fontSize: 28,
  //   fontWeight: 'bold',
  //   color: '#2B6CB0',
  //   marginBottom: 20,
  // },
  card: {
    width: '100%',
    backgroundColor: '#ffffff',
    padding: 28,
    borderRadius: 16,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 4 },
    shadowRadius: 8,
    elevation: 5,
  },
  // subtitle: {
  //   fontSize: 18,
  //   color: '#4A5568',
  //   marginBottom: 20,
  //   textAlign: 'center',
  // },
  label: {
  fontSize: 16,
  fontWeight: '700',
  color: '#2D3748',
  marginBottom: 10,
  marginTop: 10,
},
labelContainer: {
  flexDirection: 'row',
  alignItems: 'center',
  marginBottom: 8,
  marginTop: 10,
},
icon: {
  marginRight: 8,
},
labelText: {
  fontSize: 16,
  fontWeight: '700',
  color: '#2D3748',
},

  input: {
    backgroundColor: '#F7FAFC',
    borderRadius: 12,
    padding: 14,
    marginBottom: 16,
    fontSize: 16,
    borderWidth: 1,
    borderColor: '#CBD5E0',
    color: '#2D3748',
  },
  button: {
    backgroundColor: '#2B6CB0',
    paddingVertical: 14,
    borderRadius: 12,
    alignItems: 'center',
    marginTop: 6,
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 17,
    fontWeight: '600',
  },
});