import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Alert, Image, ScrollView } from 'react-native';
import * as DocumentPicker from 'expo-document-picker';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';

export default function UploadScreen() {
  const [fileName, setFileName] = useState([]);

  const pickDocument = async () => {
    try {
      const result = await DocumentPicker.getDocumentAsync({ type: "*/*", multiple: true });

      if (result.assets && result.assets.length > 0) {
        const fileNames = result.assets.map(file => file.name);
        setFileName(fileNames);
        Alert.alert('Archivos seleccionados', fileNames.join('\n'));
      } else {
        Alert.alert('No se seleccionó ningún archivo');
      }
    } catch (error) {
      console.error("Error al seleccionar documentos:", error);
      Alert.alert('Error al seleccionar archivos');
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      {/* Logo y encabezado */}
      <Image source={require('../assets/logo.png')} style={styles.logo} />

      <View style={styles.card}>
        <Image source={require('../assets/upload.png')} style={styles.image} />

        <Text style={styles.title}>Sube tu tarea</Text>
        <Text style={styles.subtitle}>Selecciona el archivo correspondiente a la materia</Text>

        <TouchableOpacity style={styles.button} onPress={pickDocument}>
          <Icon name="file-upload-outline" size={24} color="#fff" />
          <Text style={styles.buttonText}>Seleccionar archivo</Text>
        </TouchableOpacity>
      </View>

      {/* Mostrar archivos fuera del card */}
      {fileName.length > 0 && (
        <View style={styles.fileBox}>
          <Icon name="file-document" size={20} color="#2B6CB0" />
          <View>
            {fileName.map((name, index) => (
              <Text key={index} style={styles.fileText}>{name}</Text>
            ))}
          </View>
        </View>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: '#E6F0FA',
    alignItems: 'center',
  },
  logo: {
    width: 135,
    height: 135,
    marginBottom: 10,
    resizeMode: 'contain',
  },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 20,
    width: '100%',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 4 },
    shadowRadius: 6,
    elevation: 3,
  },
  image: {
    width: 120,
    height: 120,
    marginBottom: 20,
    resizeMode: 'contain',
  },
  title: {
    fontSize: 20,
    fontWeight: '700',
    color: '#2B6CB0',
    marginBottom: 6,
  },
  subtitle: {
    fontSize: 15,
    color: '#4A5568',
    marginBottom: 18,
    textAlign: 'center',
  },
  button: {
    flexDirection: 'row',
    backgroundColor: '#2B6CB0',
    paddingVertical: 12,
    paddingHorizontal: 18,
    borderRadius: 10,
    alignItems: 'center',
    gap: 8,
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
  },
  fileBox: {
    marginTop: 24,
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#C6D9F1',
    padding: 12,
    borderRadius: 10,
    width: '100%',
  },
  fileText: {
    marginLeft: 10,
    marginRight:10,
    fontSize: 14.5,
    color: '#2D3748',
  },
});
